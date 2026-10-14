#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

CONFIG = json.loads(r'''{"description": "Generate a markdown worksheet for changelog release notes architect reviews.", "default_title": "Changelog Release Notes Architect Review", "intro": "Generated worksheet for reviewing release-note audience fit, breaking-change visibility, and repeatable change communication workflow.", "sections": [{"heading": "Scope", "bullets": ["release process, versioning model, and current note style:", "audiences, support load, and change-risk profile:", "engineering source material and distribution channels:"]}, {"heading": "Review", "bullets": ["release-note audience fit:", "breaking-change visibility:", "repeatable change communication workflow:", "implementation constraints and operating consequences:"]}, {"heading": "Delivery", "bullets": ["release-note framework:", "change classification model:", "communication workflow recommendations:", "templates and editorial guidance:"]}]}''')

def build_document(title: str, focus: str) -> str:
    lines = [f"# {{title}}", "", CONFIG["intro"]]
    if focus:
        lines.extend(["", f"Focus: {{focus}}"])
    for section in CONFIG["sections"]:
        lines.extend(["", f"## {{section['heading']}}", ""])
        for bullet in section["bullets"]:
            lines.append(f"- {{bullet}}")
    return "\n".join(lines) + "\n"

def main() -> None:
    parser = argparse.ArgumentParser(description=CONFIG["description"])
    parser.add_argument("--title", default=CONFIG["default_title"])
    parser.add_argument("--focus", default="")
    parser.add_argument("--output", default="")
    args = parser.parse_args()
    rendered = build_document(args.title, args.focus)
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")

if __name__ == "__main__":
    main()
