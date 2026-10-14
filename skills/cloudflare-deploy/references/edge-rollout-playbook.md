# Edge Rollout Playbook

Use this reference when a Cloudflare deployment decision affects runtime shape, data consistency, or rollback safety, not just where static files get published.

## Key decisions

- Choose Pages, Workers, Durable Objects, KV, D1, Queues, and R2 based on runtime behavior instead of product branding.
- Define cache boundaries and consistency expectations before wiring data access at the edge.
- Separate preview, staging, and production secrets and bindings so rollouts do not leak across environments.

## Execution rules

- Map routes, build artifacts, and edge bindings explicitly so the deployment shape matches the request path design.
- Treat cache headers, purge strategy, and stale-content behavior as part of the app contract.
- Add health checks, preview validation, and rollback notes before promoting a deployment that changes runtime behavior.

## Quality bar

- A deployment should be reproducible from config, not dependent on hidden dashboard toggles.
- Operators should know what can fail regionally, what is eventually consistent, and how to back out safely.
