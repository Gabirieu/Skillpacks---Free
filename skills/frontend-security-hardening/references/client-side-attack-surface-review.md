# Client-Side Attack Surface Review

Use this reference when the frontend handles untrusted content, sensitive session state, or privileged flows that cannot rely on the UI being honest.

## Key decisions

- Map where untrusted HTML, URLs, markdown, query params, and third-party widgets can influence the DOM.
- Choose how session state is represented in the client, and what never belongs in browser-visible storage.
- Define which routes, actions, and feature flags are cosmetic in the UI versus enforced on the server.

## Execution rules

- Sanitize or avoid rendering unsafe HTML and treat URL composition, redirects, and downloads as injection surfaces.
- Prefer patterns that keep refresh tokens and durable secrets out of JavaScript-accessible storage.
- Audit copy-to-clipboard flows, debug panels, error screens, and client caches for accidental data exposure.

## Quality bar

- The app should stay safe even when client state is stale, manipulated, or inspected by an attacker.
- Security should not depend on hidden UI conditions that the server never verifies.
