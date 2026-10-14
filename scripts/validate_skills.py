#!/usr/bin/env python3
"""Validate the FGDevs SkillPacks Free library without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {
    "accessibility-remediation-planner",
    "changelog-release-notes-architect",
    "checkout-conversion-ux-architect",
    "cloudflare-deploy",
    "code-review-rubric-architect",
    "create-plan",
    "frontend-security-hardening",
    "landingpage-conversion-architect",
    "operating-procedures-author",
    "prompt-ops-governance-architect",
}
REFERENCES = re.compile(r"\x60((?:assets|references|scripts)/[A-Za-z0-9_.\-/]+)\x60")
BAD_NAMES = {"CLAUDE_NOTES.md", "manifest.txt"}
SENSITIVE = re.compile(
    r"(^|/)(?:\.env(?:\.|$)|id_rsa(?:\.|$)|credentials(?:\.|$)|"
    r"\.aws/|secret(?:s)?\.(?:json|yaml|yml|txt)|.*\.pem$)",
    re.IGNORECASE,
)


def validate() -> list[str]:
    errors = []
    if not SKILLS.is_dir():
        return ["Pasta skills/ não encontrada."]

    actual = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    if actual != EXPECTED:
        errors.append(
            f"Skills divergentes. Ausentes: {sorted(EXPECTED - actual)}; "
            f"inesperadas: {sorted(actual - EXPECTED)}"
        )

    for item in sorted(SKILLS.rglob("*")):
        relative = item.relative_to(ROOT).as_posix()
        if item.is_symlink():
            errors.append(f"Link simbólico não permitido: {relative}")
        if SENSITIVE.search(relative):
            errors.append(f"Caminho potencialmente sensível: {relative}")
        if item.name in BAD_NAMES:
            errors.append(f"Arquivo redundante: {relative}")

    for name in sorted(actual):
        folder = SKILLS / name
        skill_file = folder / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"SKILL.md ausente: {name}")
            continue
        contents = skill_file.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", contents, re.DOTALL)
        if not frontmatter:
            errors.append(f"Frontmatter inválido: {name}")
            continue
        header = frontmatter.group(1)
        declared = re.search(r"^name:\s*(.+?)\s*$", header, re.MULTILINE)
        if not declared or declared.group(1).strip("'\"") != name:
            errors.append(f"Nome de skill incorreto: {name}")
        if not re.search(r"^description:\s*\S", header, re.MULTILINE):
            errors.append(f"Descrição ausente: {name}")

        for relative in set(REFERENCES.findall(contents)):
            if ".." in Path(relative).parts or not (folder / relative).is_file():
                errors.append(f"Referência inválida: {name}/{relative}")

        for script in folder.rglob("*.py"):
            try:
                compile(script.read_text(encoding="utf-8"), str(script), "exec")
            except SyntaxError as error:
                errors.append(f"Erro de sintaxe: {script.relative_to(ROOT)}: {error}")

    # Verificação editorial de arquivos distribuídos publicamente.
    public_files = [
        ROOT / "README.md",
        ROOT / "CHANGELOG.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / "SECURITY.md",
        ROOT / "docs" / "CATALOG.md",
        ROOT / "docs" / "INSTALLATION.md",
        ROOT / "docs" / "releases" / "v1.2.md",
        *SKILLS.rglob("*.md"),
        *SKILLS.rglob("*.py"),
    ]
    private_email = re.compile(r"\b[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}\b")
    personal_home = re.compile(
        r"(?:[A-Za-z]:\\Users\\[A-Za-z0-9_.-]+|"
        r"/(?:Users|home)/[A-Za-z0-9_.-]+)"
    )
    token_like = re.compile(r"(?:ghp_|github_pat_|AKIA)[A-Za-z0-9_]{12,}")
    for file in public_files:
        if not file.is_file():
            errors.append(f"Arquivo de documentação ausente: {file.relative_to(ROOT)}")
            continue
        contents = file.read_text(encoding="utf-8")
        path = file.relative_to(ROOT).as_posix()
        if private_email.search(contents):
            errors.append(f"Possível e-mail exposto em: {path}")
        if personal_home.search(contents):
            errors.append(f"Possível diretório pessoal exposto em: {path}")
        if token_like.search(contents):
            errors.append(f"Possível token exposto em: {path}")
    return errors


if __name__ == "__main__":
    findings = validate()
    if findings:
        print("\n".join(f"ERRO: {issue}" for issue in findings), file=sys.stderr)
        raise SystemExit(1)
    print(f"OK: {len(EXPECTED)} skills verificadas, referências e scripts íntegros.")
