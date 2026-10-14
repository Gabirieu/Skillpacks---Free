#!/usr/bin/env python3
import argparse
from pathlib import Path

CONFIG = {
    "description": "Generate a markdown worksheet for checkout-conversion-ux-architect reviews.",
    "default_title": "Checkout Conversion UX Architect Review",
    "intro": "Generated worksheet for reviewing checkout flow confidence and clarity, validation and recovery design, and conversion-safe UX sequencing.",
    "scope": ["current flows, UI patterns, and usability issues", "accessibility, device, and implementation constraints", "measurement, QA process, and launch expectations"],
    "review": ["checkout flow confidence and clarity", "validation and recovery design", "conversion-safe UX sequencing", "implementation constraints and operating consequences"],
    "delivery": ["experience architecture review", "interaction, content, or validation recommendations", "QA, rollout, and follow-up checklist", "ownership and operating-model recommendations"],
}


def build_document(title: str, focus: str) -> str:
    lines = [f"# {title}", "", CONFIG["intro"]]
    if focus:
        lines.extend(["", f"Focus: {focus}"] )
    for heading, bullets in [("Scope", CONFIG["scope"]), ("Review", CONFIG["review"]), ("Delivery", CONFIG["delivery"])]:
        lines.extend(["", f"## {heading}", ""])
        for bullet in bullets:
            lines.append(f"- {bullet}:")
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
