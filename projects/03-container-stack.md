# Reproducible container stack

**Intermediate · local Docker runtime**

Run a small application and a disposable data service through Compose.

## Build

- Build the app image and run it as a non-root user.
- Use service names for networking and a volume for sample data.
- Bind developer-facing ports to localhost.
- Include meaningful health checks and documented prerequisites.

## Demonstrate

- Rebuild from a clean checkout.
- Stop the data service and observe how the application behaves.
- Restore sample data into a fresh volume and verify it.

## Deliver

Compose configuration, build instructions, backup/restore notes and a failure investigation.

## Clean up

Run docker compose down; remove the specific disposable data volume only after the restore exercise is complete.

## Explain this tradeoff

Which state survives container replacement, and how do you know?

[Resources](../resources/containers.md) · [All projects](README.md) · [Architecture decision template](../templates/architecture-decision.md)
