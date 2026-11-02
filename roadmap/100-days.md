# A 100-day practice roadmap

A suggested sequence for roughly 60–90 minutes of practice per day. Stretch or repeat days as needed. This is a learning plan, not a promise of expertise in 100 days. Cloud labs are optional and may incur charges; local equivalents are valid when you document their limitations.

**Daily loop:** ask a question → consult one resource → build or investigate → record evidence → explain the result.

[Start here](../START-HERE.md) · [Projects](../projects/README.md) · [Resource library](../resources/README.md)

## Progress checkpoints

| Days | Evidence |
|---|---|
| 1–20 | Shell notes, request-flow diagram, Git history, automation script |
| 21–40 | One cloud design and a reproducible container stack |
| 41–60 | CI pipeline, rollback evidence, infrastructure lifecycle |
| 61–80 | Local Kubernetes deployment, observability, recovery drill |
| 81–100 | Security review, capstone, open-source contribution draft |

## Days 1–5: Get comfortable in the terminal

References: [foundations](../resources/foundations.md).

- [ ] **Day 1 — Set up your learning environment.** Record your OS, Python and Git versions. Create a learning log and run the local lab.
- [ ] **Day 2 — Navigate and inspect files.** Use pwd, ls, find and file. Explain absolute versus relative paths.
- [ ] **Day 3 — Understand permissions.** Create a disposable file, change its permissions and explain the result. Never experiment on system directories.
- [ ] **Day 4 — Understand processes.** Start the lab, find its process and stop it gracefully. Distinguish process ID from port number.
- [ ] **Day 5 — Rebuild without a tutorial.** Run the lab from memory and write a reproducible setup note.

## Days 6–10: Understand a request

References: [foundations](../resources/foundations.md).

- [ ] **Day 6 — Trace DNS.** Use dig or nslookup and describe recursive versus authoritative answers.
- [ ] **Day 7 — Inspect HTTP.** Use curl -i against the lab. Explain headers, response body and status.
- [ ] **Day 8 — Map TCP and ports.** Draw client → socket → server. Inspect listening sockets with an OS-appropriate tool.
- [ ] **Day 9 — Learn subnets and routing.** Calculate a small private subnet and explain the default route; compare a firewall with a route.
- [ ] **Day 10 — Diagnose a connection failure.** Stop the lab and distinguish connection refusal from an HTTP error. Capture evidence.

## Days 11–15: Use Git intentionally

References: [git and code](../resources/git-and-code.md).

- [ ] **Day 11 — Create a clean history.** Initialize your own practice repo, add a README and make small commits.
- [ ] **Day 12 — Work on a branch.** Create a branch, change a file, inspect the diff and merge it.
- [ ] **Day 13 — Resolve a conflict.** Create a controlled text conflict and explain how you resolved both intentions.
- [ ] **Day 14 — Review a pull request.** Open a PR in your own repo with a clear problem, change and validation description.
- [ ] **Day 15 — Explain Git history.** Draw your commit graph and distinguish a revert from rewriting history.

## Days 16–20: Automate a useful task

References: [git and code](../resources/git-and-code.md).

- [ ] **Day 16 — Read structured data.** Write a Python script that loads a local JSON file and handles invalid input.
- [ ] **Day 17 — Add a command-line interface.** Accept a filename argument and document exit codes.
- [ ] **Day 18 — Handle failures.** Simulate a missing file and malformed data. Return a useful message without a traceback for expected errors.
- [ ] **Day 19 — Check shell assumptions.** Run ShellCheck on a small script; explain quoting and pipeline exit behavior.
- [ ] **Day 20 — Ship project 1.** Finish the system-inspector brief with sample output and a setup guide.

## Days 21–25: Choose one cloud

References: [cloud](../resources/cloud.md).

- [ ] **Day 21 — Map cloud primitives.** Choose AWS, Azure or Google Cloud. Map identity, network, compute and storage concepts.
- [ ] **Day 22 — Prepare identity and billing.** Enable MFA, choose a learning account/project and configure budget alerts if you will deploy.
- [ ] **Day 23 — Learn identity boundaries.** Explain a human identity, workload identity and least privilege using provider documentation.
- [ ] **Day 24 — Learn compute tradeoffs.** Compare a VM, managed container and function for one workload.
- [ ] **Day 25 — Plan the first deployment.** Draw the architecture, estimate cost and write cleanup steps before creating resources.

## Days 26–30: Build a small cloud foundation

References: [cloud](../resources/cloud.md).

- [ ] **Day 26 — Inspect a virtual network.** Draw public/private addressing, routing and ingress rules for your chosen cloud.
- [ ] **Day 27 — Practice object storage.** Use a sandbox or document a storage design. Avoid public write access; decide whether public read is necessary.
- [ ] **Day 28 — Deploy one small service.** Follow a provider guide in your learning environment, or document a local equivalent if avoiding cloud costs.
- [ ] **Day 29 — Add logs and ownership.** Find service logs and record the resource owner, region and intended lifetime.
- [ ] **Day 30 — Ship project 2 and clean up.** Verify the deployment evidence, then delete lab resources and check the remaining inventory.

## Days 31–35: Understand containers

References: [containers](../resources/containers.md).

- [ ] **Day 31 — Inspect an image.** Explain layers, image tags, image digests and the difference between build and runtime.
- [ ] **Day 32 — Build the lab image.** Build the supplied Dockerfile and record the build output and Python version.
- [ ] **Day 33 — Run with explicit boundaries.** Bind the container to localhost, inspect its user and explain port mapping.
- [ ] **Day 34 — Pass configuration.** Run the image with a different environment value. Keep secrets out of the image.
- [ ] **Day 35 — Investigate failure.** Trigger the lab’s failure mode, inspect logs and record the health-check behavior.

## Days 36–40: Make local environments repeatable

References: [containers](../resources/containers.md).

- [ ] **Day 36 — Use Compose.** Start the supplied Compose lab, inspect its service and run its health check.
- [ ] **Day 37 — Understand persistence.** Add a disposable data service in your own project and distinguish volume lifetime from container lifetime.
- [ ] **Day 38 — Understand service discovery.** Connect services by their Compose service names rather than fixed container IPs.
- [ ] **Day 39 — Practice backup and restore.** Back up sample data and restore it into a fresh disposable service.
- [ ] **Day 40 — Ship project 3.** Publish the reproducible stack, failure notes and exact cleanup commands.

## Days 41–45: Build the first pipeline

References: [delivery](../resources/delivery.md).

- [ ] **Day 41 — Run checks locally.** Run a small application’s tests and document its pass/fail exit behavior.
- [ ] **Day 42 — Add a CI workflow.** Run checks on pushes and pull requests with read-only default permissions.
- [ ] **Day 43 — Break the build deliberately.** Introduce a failing test on a practice branch and inspect the CI failure.
- [ ] **Day 44 — Publish a build artifact.** Create an artifact or image in your own repo and record its immutable identity.
- [ ] **Day 45 — Review workflow trust.** Explain why a PR from an untrusted fork should not receive deployment credentials.

## Days 46–50: Learn controlled releases

References: [delivery](../resources/delivery.md).

- [ ] **Day 46 — Version a release.** Apply semantic versioning to three sample changes and write release notes.
- [ ] **Day 47 — Design deployment gates.** Describe how tests, approval and rollout checks protect one environment.
- [ ] **Day 48 — Plan identity without long-lived keys.** Read your provider’s workload federation/OIDC guide and sketch the trust policy.
- [ ] **Day 49 — Practice rollback.** Deploy a bad local version and recover to a known image or commit.
- [ ] **Day 50 — Ship project 4.** Document build → test → artifact → release → rollback with evidence.

## Days 51–55: Define infrastructure as code

References: [infrastructure as code](../resources/infrastructure-as-code.md).

- [ ] **Day 51 — Choose Terraform or OpenTofu.** Install one tool using its official instructions and explain its provider model.
- [ ] **Day 52 — Read a plan.** Use a local or sandbox tutorial; distinguish proposed creation, update and deletion.
- [ ] **Day 53 — Understand state.** Explain why state may contain secrets and how concurrent edits are controlled.
- [ ] **Day 54 — Create a small module.** Add typed inputs, validation and outputs to your own sample.
- [ ] **Day 55 — Exercise a full lifecycle.** Plan, apply and destroy in a disposable environment; verify teardown.

## Days 56–60: Make infrastructure reviewable

References: [infrastructure as code](../resources/infrastructure-as-code.md).

- [ ] **Day 56 — Run formatting and validation.** Add fmt and validate checks for your chosen tool.
- [ ] **Day 57 — Inspect policy checks.** Run a linter or policy scanner and investigate a finding before suppressing it.
- [ ] **Day 58 — Observe drift.** Change one sandbox setting manually, inspect the next plan and explain reconciliation.
- [ ] **Day 59 — Review environment separation.** Describe state ownership, credential scope and the boundary between dev and production.
- [ ] **Day 60 — Ship project 5.** Publish reusable infrastructure with diagrams, cost estimates and a teardown checklist.

## Days 61–65: Understand Kubernetes objects

References: [containers](../resources/containers.md).

- [ ] **Day 61 — Create a local cluster.** Choose kind or minikube and document memory/CPU needs and deletion steps.
- [ ] **Day 62 — Deploy the app.** Create a Deployment and Service for your own lab application.
- [ ] **Day 63 — Use probes intentionally.** Separate readiness from liveness and explain what happens during an unhealthy state.
- [ ] **Day 64 — Inspect scheduling.** Set resource requests and limits; inspect events when a Pod cannot schedule.
- [ ] **Day 65 — Recover a workload.** Delete a lab Pod and explain why its controller recreates it.

## Days 66–70: Reconcile and roll back

References: [delivery](../resources/delivery.md).

- [ ] **Day 66 — Make configuration explicit.** Use ConfigMaps for nonsecret data and explain that base64 alone is not secret encryption.
- [ ] **Day 67 — Package a small app.** Render a Helm chart and review the resulting manifests before installation.
- [ ] **Day 68 — Choose one GitOps tool.** Compare Argo CD and Flux briefly, then install only one in the disposable cluster.
- [ ] **Day 69 — Observe reconciliation.** Change desired state and document how drift is detected and corrected.
- [ ] **Day 70 — Ship project 6.** Show rollout, failure, rollback and full cluster cleanup.

## Days 71–75: Observe behavior

References: [observability and sre](../resources/observability-and-sre.md).

- [ ] **Day 71 — Structure your logs.** Include timestamp, severity and request context; avoid logging secrets or personal data.
- [ ] **Day 72 — Collect metrics.** Count requests and errors with stable labels; distinguish counters and gauges.
- [ ] **Day 73 — Build a useful dashboard.** Show request rate, errors and latency and explain the question each panel answers.
- [ ] **Day 74 — Trace one request.** Instrument a small request path or diagram the spans you would need.
- [ ] **Day 75 — Investigate a symptom.** Create a controlled failure and correlate logs, metrics and traces.

## Days 76–80: Practice reliability

References: [observability and sre](../resources/observability-and-sre.md).

- [ ] **Day 76 — Define user-visible success.** Choose a meaningful SLI; do not assume a process being alive means users are happy.
- [ ] **Day 77 — Set an SLO.** Define a target and time window and calculate its corresponding error budget.
- [ ] **Day 78 — Design an actionable alert.** Write the symptom, threshold, owner and first investigation step.
- [ ] **Day 79 — Run a game day.** Break only your disposable lab, record detection and recovery times, then restore it.
- [ ] **Day 80 — Ship project 7.** Publish a dashboard, runbook and blameless incident review.

## Days 81–85: Protect systems and budgets

References: [security and cost](../resources/security-and-cost.md).

- [ ] **Day 81 — Review credentials.** Inventory how the app and pipeline authenticate; remove unused access and avoid committed credentials.
- [ ] **Day 82 — Scan the image.** Run Trivy, investigate findings and rebuild with fixes where appropriate.
- [ ] **Day 83 — Check secret hygiene.** Scan your own repository with Gitleaks; use synthetic data for demonstrations.
- [ ] **Day 84 — Review cost drivers.** List the main billable resources, idle costs and ownership tags in your design.
- [ ] **Day 85 — Record a security review.** Document threat boundaries, mitigations, remaining risks and cleanup evidence.

## Days 86–90: Read real engineering work

References: [engineering blogs](../resources/engineering-blogs.md).

- [ ] **Day 86 — Study Cloudflare.** Read the June 21, 2022 outage report and draw a timeline from the source.
- [ ] **Day 87 — Study another incident.** Choose a GitHub or GitLab report and compare recovery constraints.
- [ ] **Day 88 — Read one paper.** Use the paper-review template for GFS, Borg or Raft and list the assumptions.
- [ ] **Day 89 — Read an engineer’s explanation.** Choose a writer from the catalog and reproduce one small technique.
- [ ] **Day 90 — Revisit fundamentals.** Answer ten practice questions without notes, then revise incorrect explanations.

## Days 91–95: Build the capstone

References: [architecture](../resources/architecture.md).

- [ ] **Day 91 — Write requirements.** Choose a tiny service with a clear user and explicit reliability and cost constraints.
- [ ] **Day 92 — Document decisions.** Draw the system and record a tradeoff in an architecture decision record.
- [ ] **Day 93 — Build the delivery path.** Connect your app, tests, image build and reproducible environment.
- [ ] **Day 94 — Prove recovery.** Demonstrate one failure, restore data if relevant, and roll back a bad release.
- [ ] **Day 95 — Ship project 8.** Finish the capstone with setup, operations, evidence and cleanup.

## Days 96–100: Contribute and explain

References: [open source and people](../resources/open-source-and-people.md).

- [ ] **Day 96 — Choose an upstream project.** Read its contributor guide, issue activity and expected development setup.
- [ ] **Day 97 — Trace a behavior.** Follow one issue or feature through documentation, code and tests.
- [ ] **Day 98 — Prepare a small contribution.** Improve a real doc/example/test after checking scope and maintainer expectations.
- [ ] **Day 99 — Practice a technical walkthrough.** Explain your capstone’s request flow, failure mode and tradeoffs in five minutes.
- [ ] **Day 100 — Review and choose the next gap.** Score the portfolio rubric, write a retrospective and choose a focused next month.

## Review every five days

Close your notes and explain one mechanism. Rebuild one step from memory. Identify one mistake in your earlier understanding. Write the next experiment. If you cannot explain a prerequisite yet, spend another session on it before moving on.
