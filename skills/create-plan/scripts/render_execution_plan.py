#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

CONFIG = json.loads(r'''{"sections":[{"heading":"Objective","bullets":["Goal:","Constraints and non-goals:","Definition of done:"]},{"heading":"Ordered steps","bullets":["Step 1:","Step 2:","Step 3:"]},{"heading":"Risk and validation","bullets":["Dependencies or blockers:","Risks or decisions to watch:","Checks that confirm the plan worked:"]}],"description":"Render an execution-plan worksheet.","intro":"Generated worksheet for compressing a coding task into a plan that is concrete and easy to execute.","default_title":"Execution Plan"}''')

def build_document(title: str, focus: str) -> str:
    lines = [f"# {title}", "", CONFIG["intro"]]
    if focus:
        lines.extend(["", f"Focus: {focus}"])
    for section in CONFIG["sections"]:
        lines.extend(["", f"## {section['heading']}", ""])
        for bullet in section["bullets"]:
            lines.append(f"- {bullet}")
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
