#!/usr/bin/env python3
from pathlib import Path
import argparse

TITLE = "Prompt Ops Governance Architect"
SKILL = "prompt-ops-governance-architect"

TEMPLATE = """# {title} worksheet

## Scenario
- Context:
- Problem:
- Why now:

## Review
- Current state:
- Risks:
- Dependencies:
- Ownership:

## Target direction
- Proposed approach:
- Tradeoffs:
- Rollout considerations:

## Validation
- Acceptance criteria:
- Evidence to capture:
- Next actions:
"""

parser = argparse.ArgumentParser(description='Render a markdown worksheet for this skill.')
parser.add_argument('-o', '--out', default=f'{SKILL}-worksheet.md')
args = parser.parse_args()
Path(args.out).write_text(TEMPLATE.format(title=TITLE), encoding='utf-8')
print(f'Wrote {args.out}')
