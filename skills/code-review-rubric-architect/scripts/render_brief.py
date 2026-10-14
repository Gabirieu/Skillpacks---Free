#!/usr/bin/env python3
from pathlib import Path
from textwrap import dedent
out = Path(__file__).resolve().parents[1] / "IMPLEMENTATION_BRIEF.md"
out.write_text(dedent("""    # Implementation Brief - Code Review Rubric Architect

Skill: `code-review-rubric-architect`
Category: Developer Workflow & Delivery

## Objective
Use when creating code review rubrics, decision standards, escalation rules, and coaching structure for engineering teams.

## Recommended direction
-

## Rollout notes
-

## Validation notes
-
"""), encoding="utf-8")
print(f"Wrote {out}")
