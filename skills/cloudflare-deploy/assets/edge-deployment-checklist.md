# Edge Deployment Checklist

Use this asset when an edge deployment needs a clean rollout and runtime-boundary review before promotion.

## Runtime shape

- Choose Pages, Workers, Durable Objects, KV, D1, R2, or Queues according to real runtime behavior.
- Map request paths, storage bindings, and region or consistency assumptions explicitly.
- List environment-specific bindings and secrets that differ across preview and production.

## Rollout controls

- Define cache headers, purge strategy, and stale-content behavior as part of the deployment contract.
- Note rollback path, health checks, and preview validation requirements before promotion.
- Capture local-parity or testing constraints that could hide production-only failures.

## Validation

- Test critical routes, edge storage reads or writes, and failure behavior under missing bindings.
- Confirm secrets, CORS, auth, and origin communication remain environment-safe.
- List post-deploy checks for cache correctness, region behavior, and data access.
