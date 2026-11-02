# Resource library

**144 curated resources across 15 categories.** Each has an original annotation and a practical next step.

Labels describe the linked resource, not a guarantee of permanent access. “Free” reading does not cover cloud usage, optional products, certification exams or every linked sub-resource.

| Category | Resources |
|---|---:|
| [01 · Foundations, Linux & networking](foundations.md) | 10 |
| [02 · Git, Python & automation](git-and-code.md) | 7 |
| [03 · Cloud: choose one provider](cloud.md) | 14 |
| [04 · Containers & Kubernetes](containers.md) | 14 |
| [05 · Infrastructure as code](infrastructure-as-code.md) | 11 |
| [06 · CI/CD, GitOps & releases](delivery.md) | 9 |
| [07 · Observability, SRE & incidents](observability-and-sre.md) | 11 |
| [08 · Security, supply chain & cost](security-and-cost.md) | 9 |
| [09 · System design & data](architecture.md) | 10 |
| [10 · Engineering blogs worth reading](engineering-blogs.md) | 10 |
| [11 · Outage stories & postmortems](outage-stories.md) | 7 |
| [12 · Papers: systems first, AI optional](papers.md) | 7 |
| [13 · Open source, people & practice collections](open-source-and-people.md) | 18 |
| [14 · Community projects from my stars](community-projects.md) | 4 |
| [15 · Optional AI & MLOps extension](ai-and-mlops.md) | 3 |

## Search locally

Requires Python 3.11+; no packages or API keys.

```bash
python3 scripts/catalog.py search kubernetes
python3 scripts/catalog.py search "cost" --level Beginner
python3 scripts/catalog.py search --category papers
```

The catalog is in [JSON](../data/resources.json). Category pages are generated so descriptions stay consistent. See [maintenance instructions](../MAINTENANCE.md).
