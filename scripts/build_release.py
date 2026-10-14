#!/usr/bin/env python3
"""Generate the install-ready FGDevs SkillPacks Free ZIP with SHA-256 hashes."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from validate_skills import EXPECTED, validate

ROOT = Path(__file__).resolve().parents[1]


def build(version: str, output: Path) -> None:
    if not re.fullmatch(r"v\d+\.\d+(?:\.\d+)?", version):
        raise ValueError("Versão inválida (ex.: v1.1 ou v1.2.0).")

    issues = validate()
    if issues:
        raise ValueError("Skills inválidas:\n" + "\n".join(issues))

    prefix = f"FGDevs-SkillPacks-Free-{version}"
    notes = ROOT / "docs" / "releases" / f"{version}.md"
    extras = [
        (ROOT / "README.md", "README.md"),
        (ROOT / "docs" / "CATALOG.md", "CATALOG.md"),
        (ROOT / "docs" / "INSTALLATION.md", "INSTALLATION.md"),
        (ROOT / "docs" / "Catalogo-Free.pdf", "Catalogo-Free.pdf"),
        (notes, "RELEASE_NOTES.md"),
    ]

    entries = []
    for name in sorted(EXPECTED):
        skill = ROOT / "skills" / name
        for item in sorted(skill.rglob("*")):
            if item.is_file():
                if item.is_symlink():
                    raise ValueError(f"Link simbólico não permitido: {item}")
                relative = item.relative_to(skill).as_posix()
                entries.append((f"skills/{name}/{relative}", item.read_bytes()))

    for path, name in extras:
        if not path.is_file():
            raise ValueError(f"Arquivo de release ausente: {path}")
        entries.append((name, path.read_bytes()))

    checksum = "".join(
        f"{hashlib.sha256(data).hexdigest()}  {name}\n"
        for name, data in sorted(entries)
    )
    entries.append(("SHA256SUMS.txt", checksum.encode("utf-8")))

    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as package:
        for name, data in sorted(entries):
            info = ZipInfo(f"{prefix}/{name}", date_time=(2026, 10, 14, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            package.writestr(info, data, compress_type=ZIP_DEFLATED, compresslevel=9)

    with ZipFile(output) as package:
        broken = package.testzip()
        if broken:
            raise ValueError(f"ZIP inválido: {broken}")
        count = sum(path.endswith("/SKILL.md") for path in package.namelist())
        if count != len(EXPECTED):
            raise ValueError(f"ZIP possui {count} skills, esperadas {len(EXPECTED)}.")

    print(f"ZIP verificado: {output} ({output.stat().st_size} bytes; {count} skills)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default="v1.2")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output or ROOT / "dist" / f"FGDevs-SkillPacks-Free-{args.version}.zip"
    try:
        build(args.version, output)
    except (ValueError, OSError) as error:
        print(f"ERRO: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
