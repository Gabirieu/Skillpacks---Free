#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

CONFIG = json.loads(r'''{"sections":[{"heading":"Deployment scope","bullets":["Routes or surfaces in scope:","Cloudflare products involved:","Environment or secret boundaries:"]},{"heading":"Runtime decisions","bullets":["Chosen runtime and storage fit:","Cache and consistency assumptions:","Rollback or preview strategy:"]},{"heading":"Checks","bullets":["Critical flows to validate:","Bindings or auth risks to test:","Post-deploy verification steps:"]}],"description":"Render an edge deployment review worksheet.","intro":"Generated worksheet for reviewing Cloudflare runtime choices, bindings, cache rules, and rollout safety.","default_title":"Edge Deployment Review"}''')

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
