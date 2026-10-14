# Domain Patterns - Code Review Rubric Architect

## Objective
Use when creating code review rubrics, decision standards, escalation rules, and coaching structure for engineering teams.

## Decision cues
- clarify boundaries, ownership, and invariants before changing implementation details
- prefer explicit rollout and rollback criteria instead of informal assumptions
- keep evidence and reviewability visible from the start

## Common failure modes
- ambiguous ownership or hidden dependencies
- rollout complexity underestimated
- missing observability, validation, or approval checkpoints
- documentation that is too vague for the next team to execute safely

## Practical guidance
- start from current-state mapping
- separate mandatory controls from optional improvements
- define what must be true before calling the work complete
