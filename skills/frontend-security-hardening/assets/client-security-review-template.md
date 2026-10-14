# Client Security Review Template

Use this asset when a frontend needs a concrete browser-side security review instead of general cautionary notes.

## Attack surface

- List untrusted HTML, URL, query param, postMessage, clipboard, and third-party widget inputs.
- State which tokens, secrets, or session indicators are exposed to the browser and why.
- Map route guards, redirects, and client-visible permission signals that affect risk.

## Control review

- Check sanitization, CSP, script provenance, and download or redirect safety.
- Note where client state is trusted too far and what the server must still enforce.
- Capture browser cache, storage, error screen, and debug surface exposure.

## Validation

- Run XSS-style payload, stale-session, and route-bypass checks for the affected flows.
- Confirm sensitive data does not leak through logs, storage, or rendered markup.
- Record which server-side boundaries must be cross-verified after the frontend fix.
