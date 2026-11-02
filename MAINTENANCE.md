# Maintenance and quality

## Catalog is the source of truth

`data/resources.json` contains resource records; `data/categories.json` contains category titles and introductions. `scripts/catalog.py build` generates the library index and category pages. Edit the JSON, then regenerate. CI rejects stale generated pages, duplicate IDs/URLs, missing required fields and invalid categories.

```bash
python3 scripts/catalog.py build
python3 scripts/catalog.py check
python3 scripts/check_docs.py
python3 -m unittest discover -s labs/build-break-fix -p 'test_*.py' -v
```

All local checks use the Python standard library. Python 3.11+ is the supported baseline. No dependency installation is needed.

## Link checks

```bash
python3 scripts/check_links.py --output link-report.json
```

The checker requests catalog URLs with a bounded timeout and bounded concurrency. It verifies reachability, not the editorial accuracy of every destination or subpage. It does not download article bodies. Clear client errors such as 404 fail the run. Authentication, throttling, anti-bot responses and transient server/network failures are marked for manual review. `--strict` also fails for these review states. An HTTP 200 can still be a soft 404 or a sign-in page, so editorial review remains necessary.

The weekly/manual workflow uploads a timestamped report for maintainers. It checks the catalog, not every external badge/profile link in the prose. Manual review notes for the initial edition live in [source review](docs/source-review.md). Do not represent the initial check as permanent verification.

## Editorial review

Check links that redirect or require accounts. Prefer a current canonical page, clearly label historical material and distinguish free reading from paid labs or cloud usage. Do not copy articles or repository content into this collection. Preserve original author attribution through direct source links.

When a resource disappears, look for an author-maintained replacement; otherwise remove it and regenerate. A large collection should still have an obvious starting point.

## Lab maintenance

The lab deliberately has no third-party Python dependencies. Its HTTP tests verify the healthy path, simulated user failure, readiness/liveness distinction, unknown routes and recovery. Container CI builds the image and probes these states over localhost. The starter uses a versioned base-image tag; record or pin a digest when stronger reproducibility is needed.

Changes to behavior require appropriate verification. Keep failure injection confined to explicit local learning configuration.
