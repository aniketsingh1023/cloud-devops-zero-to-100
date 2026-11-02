# Build, test, release, roll back

**Intermediate · GitHub runner quotas may apply**

Deliver a tiny app through a pipeline that produces a versioned artifact and has a demonstrated rollback path.

## Build

- Run tests on pull requests with minimum permissions.
- Build an artifact or image with a traceable commit identity.
- Keep deployment identity scoped to its environment.
- Document release gates and rollback instructions.

## Demonstrate

- Show a failing test blocking a change.
- Inspect an untrusted-PR workflow’s credential boundaries.
- Recover a bad local release using a previous artifact.

## Deliver

Workflow files, release notes, artifact identity and rollback evidence.

## Clean up

Remove practice deployments and unnecessary artifacts using the service’s retention controls.

## Explain this tradeoff

What protects a deployment if an upstream action or dependency is compromised?

[Resources](../resources/delivery.md) · [All projects](README.md) · [Architecture decision template](../templates/architecture-decision.md)
