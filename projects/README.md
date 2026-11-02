# Build a portfolio you can explain

These are original **project briefs**, not claims that complete implementations are included. The [build-and-break lab](../labs/build-break-fix/README.md) is runnable starter code. Projects 1–8 are exercises for you to implement.

| Project | Environment | Main evidence |
|---|---|---|
| [System inspector](01-system-inspector.md) | Beginner · local · no cloud account | A README, sample input/output, source, and one bug investigation. |
| [Small cloud foundation](02-cloud-foundation.md) | Beginner–intermediate · usage may be billed | An architecture diagram, setup guide, access model, deployment evidence, and teardown record. |
| [Reproducible container stack](03-container-stack.md) | Intermediate · local Docker runtime | Compose configuration, build instructions, backup/restore notes and a failure investigation. |
| [Build, test, release, roll back](04-delivery-pipeline.md) | Intermediate · GitHub runner quotas may apply | Workflow files, release notes, artifact identity and rollback evidence. |
| [Reviewable infrastructure lifecycle](05-infrastructure-lifecycle.md) | Intermediate · local or paid cloud sandbox | Configuration, a diagram, redacted plan summaries, cost estimate and cleanup evidence. |
| [Local Kubernetes with GitOps](06-kubernetes-gitops.md) | Intermediate–advanced · local cluster | Manifests/chart, reconciliation notes, failure evidence and a cluster diagram. |
| [Observe and recover a service](07-observability-game-day.md) | Intermediate–advanced · local tools | Dashboard export, instrumentation, alert rationale, runbook and postmortem. |
| [A tiny production-minded platform](08-capstone.md) | Advanced · local or one paid cloud sandbox | A portfolio repository with a diagram, ADR, cost estimate, runbook, incident review and a five-minute demo. |

## Portfolio rubric

Score each dimension 0 (missing), 1 (partial) or 2 (clear, reproducible evidence). The goal is to expose gaps, not to claim professional certification.

| Dimension | What good evidence looks like |
|---|---|
| Reproducibility | A clean setup succeeds using documented prerequisites |
| Understanding | You can trace a request and explain component choices |
| Delivery | A failed check blocks release; an artifact traces to source |
| Reliability | A realistic failure has detection and a demonstrated recovery |
| Security | Identity, secrets and trust boundaries are explained |
| Cost and cleanup | An estimate, inventory and teardown are recorded |
| Communication | A diagram, decision record and concise walkthrough |

A score of 14 is the maximum. Have a peer review the evidence and choose the lowest-scoring dimension for your next improvement.
