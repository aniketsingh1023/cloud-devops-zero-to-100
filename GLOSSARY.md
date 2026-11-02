# Explain the vocabulary

Working definitions to start discussion. Product-specific behavior and guarantees must be checked in the relevant official documentation. For every term, give an example, a failure mode and a way to observe it.

| Term | Working definition | Example or question |
|---|---|---|
| API | A defined interface through which software requests behavior or data. | An HTTP endpoint that returns a deployment’s status. |
| Artifact | An output of a build that can be stored and deployed. | A container image identified by its digest. |
| Authentication | Checking the identity of a person or workload. | A service validates a signed identity token. |
| Authorization | Deciding which actions an authenticated identity may perform. | A role can read an object but cannot delete it. |
| Availability | The extent to which a service can deliver its intended function. | Measure successful requests from a user’s perspective. |
| Backup | A retained copy used to recover data. | A database snapshot stored separately from the active database. |
| Blast radius | The scope of harm a failure or change can cause. | A staged change affects one test environment first. |
| Cache | Stored results used to reduce repeated work or latency. | A frequently read object is served from memory. |
| Cache invalidation | Removing or updating cached data when it is no longer appropriate. | Delete a cached product record after its price changes. |
| CDN | A distributed system that delivers content closer to users. | Static assets are served from an edge location. |
| CI | Automated integration checks on changes. | A pull request triggers tests before merge. |
| Continuous delivery | Keeping software ready for a controlled release. | A verified artifact can be deployed when a release is approved. |
| Continuous deployment | Automatically releasing changes that pass the deployment process. | A passing change proceeds to production through automated gates. |
| Container | A process environment with operating-system isolation and resource controls. | A service runs with its own filesystem view. |
| Control plane | Components that decide or manage desired system behavior. | Kubernetes API and controllers manage workload state. |
| Data plane | Components that execute the system’s actual workload or traffic flow. | A proxy forwards a user request. |
| Deployment | An act of releasing software; also a Kubernetes workload resource. | A Kubernetes Deployment maintains replicated Pods. |
| Desired state | The configuration a controller tries to make true. | A manifest requests three replicas. |
| DNS | A distributed naming system that resolves names into records. | A hostname resolves to an address before a connection begins. |
| Drift | A difference between intended configuration and actual state. | A firewall rule changed manually differs from its IaC definition. |
| Error budget | The allowed unreliability implied by a particular SLO and measurement window. | A request-based SLO allows a bounded fraction of unsuccessful requests. |
| GitOps | Managing declarative desired state through versioned data and automatic reconciliation. | A controller pulls and applies approved configuration from Git. |
| Health check | A signal about some aspect of a service’s condition. | A readiness endpoint says whether the instance should receive traffic. |
| IAM | Identity and access management: identities, permissions and their policies. | A workload role grants access to one storage bucket. |
| IaC | Managing infrastructure through declarative configuration or programs. | A reviewed plan provisions a network and compute resources. |
| Idempotency | Repeating an operation has the same intended effect as doing it once. | A retry with the same idempotency key does not create another payment. |
| Image | A packaged filesystem and metadata used to start a container. | A tagged image can be pulled from a registry. |
| Ingress | Traffic entering a boundary; Kubernetes Ingress is a specific API resource. | A gateway routes incoming HTTP traffic to a service. |
| Latency | Time taken for a particular operation. | The p95 request latency describes a percentile, not an average. |
| Least privilege | Grant only the access required for the task. | A deployment identity cannot administer unrelated projects. |
| Liveness | A signal used to decide whether an instance needs restarting. | A liveness probe fails when the process cannot make progress. |
| Load balancer | A component that distributes traffic across backends. | Requests go only to eligible healthy instances. |
| Log | A record of an event or observation. | A structured request log contains status, duration and request context. |
| Metric | A numeric measurement observed over time. | A request counter increases as requests are handled. |
| Namespace | A named scope for organizing resources; semantics depend on the system. | A Kubernetes namespace groups API objects but is not complete isolation by itself. |
| NAT | Network address translation: rewriting address information in packets. | Private hosts share an outbound public address. |
| Observability | The ability to understand system behavior through its outputs and investigation. | Metrics, logs and traces help test a hypothesis about failed requests. |
| OIDC | An identity layer built on OAuth 2.0. | A pipeline presents an identity token for a scoped cloud role. |
| Pod | Kubernetes’ unit for scheduling one or more tightly coupled containers. | An application container and a helper share a Pod’s networking. |
| Queue | A mechanism for handing work from producers to consumers. | A worker processes a submitted job asynchronously. |
| Readiness | Whether an instance should receive workload traffic. | An app waits for required initialization before becoming ready. |
| Reconciliation | Repeatedly comparing observed state with desired state and acting on differences. | A controller recreates a missing Pod. |
| Replication | Keeping copies of data or work across instances. | A database maintains replicas for selected failure scenarios. |
| Restore | Recovering usable data or service from a backup. | A restore drill verifies a backup can actually be used. |
| Retry | Attempting an operation again after failure or uncertainty. | Exponential backoff with jitter spreads repeated attempts. |
| Rollback | Returning a deployment or configuration to a known prior state. | An operator reselects a previously working artifact. |
| RPO | Recovery point objective: the tolerated data-loss interval. | A design aims to lose no more than five minutes of committed data. |
| RTO | Recovery time objective: the targeted time to restore service. | A restore drill measures whether recovery fits a one-hour objective. |
| Scalability | The ability to handle a changing workload through appropriate resource changes. | Add workers while preserving queue-processing correctness. |
| Secret | Sensitive information that grants access or requires confidentiality. | A private key is stored outside source control. |
| SLI | A service level indicator measuring a chosen aspect of behavior. | The fraction of valid requests successfully served. |
| SLO | A target for an SLI over a stated window. | A defined proportion of valid requests succeeds over 30 days. |
| SLA | An agreement describing service commitments and consequences. | A contract specifies availability obligations and credits. |
| State | Stored information required to represent current system or tool knowledge. | IaC state maps declared resources to managed remote objects. |
| Subnet | A subdivision of an IP network. | A private CIDR block provides addresses for a workload tier. |
| Throughput | The amount of work completed per unit of time. | A worker processes 50 jobs per second under a given load. |
| TLS | A protocol for protecting transport confidentiality and integrity with authenticated peers. | A client validates a server certificate during an HTTPS connection. |
| Trace | A linked view of operations for a request or workflow. | Spans connect a gateway request to a database operation. |
| TTL | A duration after which stored or cached information expires. | A cache entry is eligible for expiry after its TTL. |
| VPC / VNet | A provider-specific virtual networking boundary and configuration model. | A learning environment has private addressing and explicit routing. |

## Check your understanding

Explain caching, queues, scalability, readiness and replication without using their names in the definitions. Draw one system that uses all five, then identify a failure that each mechanism does not solve.

[Architecture resources](resources/architecture.md) · [Fundamentals practice](practice/fundamentals.md)
