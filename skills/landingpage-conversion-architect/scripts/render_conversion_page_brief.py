#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

CONFIG = json.loads(r'''{"sections":[{"heading":"Offer scope","bullets":["Audience and promise:","Primary CTA and business goal:","Main objection or trust barrier:"]},{"heading":"Page structure","bullets":["Section sequence:","Proof and objection placement:","Responsive or content-priority concerns:"]},{"heading":"Checks","bullets":["Conversion assumptions to validate:","Analytics or experiments to run:","Content gaps to fill:"]}],"description":"Render a conversion page brief.","intro":"Generated worksheet for structuring a landing page around positioning, proof, objections, and calls to action.","default_title":"Conversion Page Brief"}''')

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
