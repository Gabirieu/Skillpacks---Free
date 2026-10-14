# Operating Procedures Author - Domain Patterns

This note supports tasks where the team needs deeper judgment for **use when authoring operating procedures, role-based step sequences, control points, exception handling, and audit-friendly operational docs.**.

## Pattern cues
- Prefer decisions that make ownership and operational responsibility explicit.
- Keep compatibility, rollout safety, and observability visible from the start.
- Treat ambiguous boundaries as design problems rather than documentation problems.
- Use progressive rollout and validation instead of one-shot migration assumptions.

## Tradeoff prompts
- What belongs in the platform layer versus the domain layer?
- Which invariants must be enforced once, and where?
- What should be optimized for: speed, safety, reversibility, or long-term simplicity?
- What failure mode becomes more likely if the design is simplified too aggressively?

## Failure modes to watch
- Hidden coupling that makes ownership or rollback unclear.
- Metrics that look healthy while user or operator outcomes are degrading.
- Exception paths, edge cases, or governance steps that only exist in tribal knowledge.
- A design that reads well on paper but cannot be supported day to day.
