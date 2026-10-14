#!/usr/bin/env python3
from pathlib import Path
import argparse

TITLE = "Accessibility Remediation Planner"
SKILL = "accessibility-remediation-planner"

TEMPLATE = """# {title} implementation brief

## Goal
- Desired outcome:

## Constraints
- Non-negotiables:
- Risks:

## Recommended plan
1. Discovery
2. Design
3. Implementation
4. Validation
5. Rollout

## Notes
- Owners:
- Metrics:
- Rollback triggers:
"""

parser = argparse.ArgumentParser(description='Render a concise implementation brief for this skill.')
parser.add_argument('-o', '--out', default=f'{SKILL}-brief.md')
args = parser.parse_args()
Path(args.out).write_text(TEMPLATE.format(title=TITLE), encoding='utf-8')
print(f'Wrote {args.out}')
