# 07 · Observability, SRE & incidents

Measure user-visible behavior, investigate failures and practice recovery. Start with logs and a useful health check.

[All categories](README.md) · [Roadmap](../roadmap/100-days.md) · [Start here](../START-HERE.md)

## Google SRE books

[Book →](https://sre.google/books/) · **Intermediate** · **Access:** Free online / print editions paid

Study reliability practices from the original publisher.

**Try this:** Read one chapter and turn a recommendation into a lab experiment.

## Prometheus introduction

[Guide →](https://prometheus.io/docs/introduction/overview/) · **Intermediate** · **Access:** Free

Learn a metrics collection and query model.

**Try this:** Collect request counts and explain counter versus gauge.

## Prometheus query basics

[Reference →](https://prometheus.io/docs/prometheus/latest/querying/basics/) · **Intermediate** · **Access:** Free

Practice the semantics of time-series queries.

**Try this:** Write a rate query and explain its time window.

## Grafana tutorials

[Lab →](https://grafana.com/tutorials/) · **Intermediate** · **Access:** Free tutorials / services vary

Build dashboards around operational questions.

**Try this:** Create a dashboard that answers whether users are seeing errors.

## OpenTelemetry documentation

[Guide →](https://opentelemetry.io/docs/) · **Intermediate** · **Access:** Free

Understand portable instrumentation and telemetry pipelines.

**Try this:** Trace one request and distinguish telemetry collection from storage.

## Grafana Loki

[Guide →](https://grafana.com/docs/loki/latest/) · **Intermediate** · **Access:** Free docs / deployment costs vary

Explore log aggregation and label choices.

**Try this:** Design labels that avoid unbounded request-ID cardinality.

## Google SRE: postmortem culture

[Guide →](https://sre.google/sre-book/postmortem-culture/) · **Intermediate** · **Access:** Free

Learn to turn incidents into actionable engineering changes.

**Try this:** Write a blameless postmortem for a deliberately broken lab.

## Google SRE: service level objectives

[Guide →](https://sre.google/sre-book/service-level-objectives/) · **Intermediate** · **Access:** Free

Connect service indicators, objectives and user expectations.

**Try this:** Define one SLI and a measurable SLO for your service.

## Awesome SRE

[Repository →](https://github.com/dastergon/awesome-sre) · **Intermediate** · **Access:** Free links / destinations vary

Explore a wider reliability reading collection.

**Try this:** Select one resource for a specific knowledge gap rather than reading everything.

## LitmusChaos

[Repository →](https://github.com/litmuschaos/litmus) · **Advanced** · **Access:** Free source / cluster compute required

Explore controlled fault experiments and reliability hypotheses.

**Try this:** Design one bounded experiment in a disposable cluster with explicit abort and recovery conditions.

## Pino structured logging

[Repository →](https://github.com/pinojs/pino) · **Intermediate** · **Access:** Free source / upstream license applies

A concrete Node.js logging implementation with redaction and transport documentation.

**Try this:** Add structured logs to a tiny Node app and verify sensitive fields are redacted.

---

Generated from [the resource catalog](../data/resources.json). Suggest edits through [the contribution guide](../CONTRIBUTING.md).
