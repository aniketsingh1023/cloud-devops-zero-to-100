# 06 · CI/CD, GitOps & releases

Build a small pipeline, deliberately break it, then add the checks that would have caught the failure.

[All categories](README.md) · [Roadmap](../roadmap/100-days.md) · [Start here](../START-HERE.md)

## GitHub Actions

[Guide →](https://docs.github.com/en/actions) · **Beginner** · **Access:** Free docs / runner quotas and billing vary

Automate repeatable repository workflows.

**Try this:** Add a test job and inspect a failed run before fixing it.

## GitHub Actions security

[Guide →](https://docs.github.com/en/actions/how-tos/secure-your-work) · **Intermediate** · **Access:** Free

Understand credentials, workflow trust and deployment security.

**Try this:** Review workflow permissions and document how untrusted PRs are handled.

## GitLab CI/CD

[Guide →](https://docs.gitlab.com/ci/) · **Intermediate** · **Access:** Free docs / runner costs vary

Learn another pipeline model and compare the concepts.

**Try this:** Translate a build-test pipeline into stages and dependencies.

## Jenkins Pipeline

[Guide →](https://www.jenkins.io/doc/book/pipeline/) · **Intermediate** · **Access:** Free docs / infrastructure required

Understand pipeline-as-code in Jenkins.

**Try this:** Read a Jenkinsfile and identify build, test and deployment boundaries.

## Argo CD

[Guide →](https://argo-cd.readthedocs.io/en/stable/) · **Intermediate** · **Access:** Free docs / cluster required

Learn declarative delivery from version-controlled desired state.

**Try this:** Change a manifest and explain sync, drift and rollback.

## Flux

[Guide →](https://fluxcd.io/flux/) · **Intermediate** · **Access:** Free docs / cluster required

Explore an alternative Kubernetes GitOps toolkit.

**Try this:** Compare reconciliation and repository layout with an Argo CD design.

## OpenGitOps principles

[Guide →](https://opengitops.dev/) · **Intermediate** · **Access:** Free

Separate GitOps principles from specific tools.

**Try this:** Explain how desired state is versioned, pulled and reconciled.

## DORA guides

[Guide →](https://dora.dev/guides/) · **Intermediate** · **Access:** Free

Connect delivery practices to outcomes and measurement.

**Try this:** Choose a delivery improvement and define how you will evaluate it.

## Semantic Versioning

[Reference →](https://semver.org/) · **Beginner** · **Access:** Free

Define a clear contract for release numbers.

**Try this:** Classify three sample changes as major, minor or patch.

---

Generated from [the resource catalog](../data/resources.json). Suggest edits through [the contribution guide](../CONTRIBUTING.md).
