# Small cloud foundation

**Beginner–intermediate · usage may be billed**

Deploy a tiny static page or service on one provider, with identity and cost controls documented.

## Build

- Choose one provider and draw its account/project and network boundaries.
- Set MFA and budget alerts; record the chosen region and cost estimate.
- Use a documented hosting path and avoid embedding credentials in code.
- Decide which endpoints must be public and explain why.

## Demonstrate

- Fetch the page or endpoint and record response behavior.
- Verify an unauthenticated user cannot perform administrative actions.
- Check the resource inventory and billing dashboard after teardown.

## Deliver

An architecture diagram, setup guide, access model, deployment evidence, and teardown record.

## Clean up

Delete all lab resources and inspect related disks, addresses, snapshots and logs; verify charges separately.

## Explain this tradeoff

What would change if this service needed private access or a second region?

[Resources](../resources/cloud.md) · [All projects](README.md) · [Architecture decision template](../templates/architecture-decision.md)
