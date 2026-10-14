#!/usr/bin/env python3
from pathlib import Path
from textwrap import dedent
out = Path(__file__).resolve().parents[1] / "REVIEW_WORKSHEET.md"
out.write_text(dedent("""    # Review Worksheet - Code Review Rubric Architect

Use this worksheet to structure discovery, decisions, rollout, and validation for `code-review-rubric-architect`.

## Goal
-

## Current state
-

## Risks
-

## Recommended direction
-

## Rollout
-

## Validation
-

## Handoff
-
"""), encoding="utf-8")
print(f"Wrote {out}")
