# Contributing

Help a learner understand something or take a useful next step. A small, well-explained addition is better than a large list without context.

## Suggest a resource

Use the resource suggestion issue template or send a focused pull request. Include:

- The original author/project and canonical HTTPS URL.
- The category, difficulty, format and access requirements.
- An original explanation of the specific learning value.
- A concrete practice task that fits the resource.
- Any account, payment, cloud billing or upstream license constraints.

Prefer official documentation and original engineering write-ups. A community resource is welcome when it teaches something clearly and adds value beyond existing entries. Disclose your connection if it is your own work. Do not submit affiliate links, pirated content, credential dumps, scraped articles or copied question banks.

## Edit the catalog

1. Edit `data/resources.json`. Use the existing field names and a stable, unique ID.
2. Use a category from `data/categories.json`. Search first to avoid duplicate URLs.
3. Write the description and practice task yourself. Link to upstream work rather than copying it.
4. Run the commands below from the repository root.
5. Explain the learning gap your change fills in the PR description.

```bash
python3 scripts/catalog.py build
python3 scripts/catalog.py check
python3 scripts/check_docs.py
python3 -m unittest discover -s labs/build-break-fix -p 'test_*.py' -v
```

For a URL change, also run `python3 scripts/check_links.py` or verify the affected URL manually. Some publishers block automated clients; record what you checked rather than removing a useful resource solely because it returned 403.

## Improve the learning material

Corrections, clearer explanations, accessibility improvements and small reproducible exercises are welcome. For a new project, include prerequisites, acceptance criteria, failure practice, cost notes and cleanup. Avoid introducing a paid service as the only way to complete a beginner exercise.

## Review expectations

Maintainers review relevance, originality, accuracy, access terms and duplication. Being popular or starred is a discovery signal, not sufficient reason for inclusion. Links can be retired if they no longer work or no longer fit the learning path.

By contributing original material, you agree to license that contribution under this repository’s MIT license. Do not submit material you do not have the right to contribute. Upstream resources retain their own licenses.
