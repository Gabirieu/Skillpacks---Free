#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

CONFIG = json.loads(r'''{"sections":[{"heading":"Surface map","bullets":["Routes or screens in scope:","Untrusted content or script inputs:","Session or token behavior involved:"]},{"heading":"Risk review","bullets":["XSS, redirect, or script-origin risk:","Client trust or route-protection gap:","Sensitive storage or cache exposure:"]},{"heading":"Checks","bullets":["Payloads or flows to validate:","Server-side boundaries to confirm:","Observability or incident hooks needed:"]}],"description":"Render a client security review worksheet.","intro":"Generated worksheet for reviewing XSS exposure, token handling, route protection, and browser trust boundaries.","default_title":"Client Security Review"}''')

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
