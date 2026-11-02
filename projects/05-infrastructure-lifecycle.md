# Reviewable infrastructure lifecycle

**Intermediate · local or paid cloud sandbox**

Provision a small environment with Terraform or OpenTofu and explain every planned change.

## Build

- Use typed inputs, outputs and a small reusable module.
- Keep state and variable secrets out of Git.
- Document state locking/ownership and environment separation.
- Run formatting, validation and a relevant policy check.

## Demonstrate

- Read and annotate a create plan and a destroy plan.
- Demonstrate drift detection in the disposable environment.
- Destroy resources and verify the provider inventory.

## Deliver

Configuration, a diagram, redacted plan summaries, cost estimate and cleanup evidence.

## Clean up

Destroy only this exercise’s state-owned resources; inspect leftovers rather than assuming destroy removed everything.

## Explain this tradeoff

How would two engineers avoid racing changes or accessing each other’s secrets?

[Resources](../resources/infrastructure-as-code.md) · [All projects](README.md) · [Architecture decision template](../templates/architecture-decision.md)
