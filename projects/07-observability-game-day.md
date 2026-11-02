# Observe and recover a service

**Intermediate–advanced · local tools**

Add useful telemetry to a service, then practice detecting and recovering from a failure.

## Build

- Collect request and error metrics with bounded labels.
- Add structured logs and trace context where helpful.
- Define an SLI, SLO and one actionable alert.
- Write a runbook before the failure exercise.

## Demonstrate

- Inject a failure only into the disposable lab.
- Measure time to detect and recover; separate observations from guesses.
- Write a blameless review with an owner and verification for each action.

## Deliver

Dashboard export, instrumentation, alert rationale, runbook and postmortem.

## Clean up

Stop local collectors and remove disposable telemetry data if no longer needed.

## Explain this tradeoff

Would your alert detect a user-visible failure while every process is still alive?

[Resources](../resources/observability-and-sre.md) · [All projects](README.md) · [Architecture decision template](../templates/architecture-decision.md)
