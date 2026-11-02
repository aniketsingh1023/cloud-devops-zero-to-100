# Local Kubernetes with GitOps

**Intermediate–advanced · local cluster**

Deploy a small application into kind or minikube, then reconcile desired state from Git.

## Build

- Use a Deployment, Service, resource requests/limits and probes.
- Keep nonsecret configuration separate from the image.
- Choose Argo CD or Flux and document repository reconciliation.
- Record an immutable image identity for reproducibility.

## Demonstrate

- Observe Pod replacement after deletion.
- Trigger an unhealthy deployment and inspect events and readiness.
- Revert desired state and demonstrate recovery.

## Deliver

Manifests/chart, reconciliation notes, failure evidence and a cluster diagram.

## Clean up

Remove the exercise’s workloads and delete its specific local cluster.

## Explain this tradeoff

What happens when the cluster cannot reach Git or the image registry?

[Resources](../resources/containers.md) · [All projects](README.md) · [Architecture decision template](../templates/architecture-decision.md)
