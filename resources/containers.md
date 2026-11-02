# 04 · Containers & Kubernetes

Learn images and container networking first. Use a local cluster before paying for a managed Kubernetes service.

[All categories](README.md) · [Roadmap](../roadmap/100-days.md) · [Start here](../START-HERE.md)

## Docker getting started

[Guide →](https://docs.docker.com/get-started/) · **Beginner** · **Access:** Free docs / product terms vary

Official introduction to images and containers.

**Try this:** Containerize the local lab and explain image versus container.

## Docker Compose

[Guide →](https://docs.docker.com/compose/) · **Beginner** · **Access:** Free

Define a repeatable local multi-service environment.

**Try this:** Run two services and explain their network and volume lifecycle.

## Dockerfile reference

[Reference →](https://docs.docker.com/reference/dockerfile/) · **Intermediate** · **Access:** Free

Understand build instructions and their behavior.

**Try this:** Explain cache invalidation and run your image as a non-root user.

## Kubernetes concepts

[Reference →](https://kubernetes.io/docs/concepts/) · **Intermediate** · **Access:** Free

Build a vocabulary for the Kubernetes API.

**Try this:** Explain the relationship between a Deployment, Pod and Service.

## Kubernetes tutorials

[Lab →](https://kubernetes.io/docs/tutorials/) · **Intermediate** · **Access:** Free docs / runtime costs vary

Official guided practice with Kubernetes features.

**Try this:** Deploy an app and describe how readiness differs from liveness.

## kind

[Tool →](https://kind.sigs.k8s.io/) · **Intermediate** · **Access:** Free / local compute

Create disposable Kubernetes clusters in containers.

**Try this:** Create and delete a local cluster; document prerequisites and cleanup.

## minikube

[Tool →](https://minikube.sigs.k8s.io/docs/) · **Beginner** · **Access:** Free / local compute

An alternative local Kubernetes learning environment.

**Try this:** Choose a supported driver and inspect a running local cluster.

## Helm documentation

[Guide →](https://helm.sh/docs/) · **Intermediate** · **Access:** Free

Package and configure Kubernetes resources.

**Try this:** Template a small chart and inspect output before installing it.

## Kubernetes the Hard Way

[Repository →](https://github.com/kelseyhightower/kubernetes-the-hard-way) · **Advanced** · **Access:** Free guide / compute required

Investigate cluster components by building them manually.

**Try this:** Read prerequisites and diagram the control plane before provisioning anything.

## Kubernetes source

[Repository →](https://github.com/kubernetes/kubernetes) · **Advanced** · **Access:** Free

Read a large infrastructure project’s implementation and tests.

**Try this:** Trace a small behavior from an issue to code and a test.

## Kubernetes contributor onboarding

[Guide →](https://www.kubernetes.dev/docs/onboarding/) · **Intermediate** · **Access:** Free

Understand contribution expectations and community structure.

**Try this:** Find the right SIG and read its contribution guide.

## Kubernetes Kickstarter

[Repository →](https://github.com/LondheShubham153/kubestarter) · **Beginner** · **Access:** Free repo / local or usage-billed cloud

Architecture notes, examples and companion videos for Kubernetes practice.

**Try this:** Start with a local Deployment and Service and explain each field you keep.

## Meshery

[Repository →](https://github.com/meshery/meshery) · **Advanced** · **Access:** Free source / platform and compute terms vary

A real cloud-native project for platform-engineering study and contribution.

**Try this:** Read its contributor guide and trace one infrastructure-management operation through the code.

## Helm Dashboard

[Repository →](https://github.com/komodorio/helm-dashboard) · **Intermediate** · **Access:** Free source / local or cluster compute

Inspect chart revisions and release differences through a community interface.

**Try this:** Compare two release manifests in a disposable cluster and explain the proposed rollback.

---

Generated from [the resource catalog](../data/resources.json). Suggest edits through [the contribution guide](../CONTRIBUTING.md).
