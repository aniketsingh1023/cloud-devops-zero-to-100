# System inspector

**Beginner · local · no cloud account**

Build a Python CLI that reports basic machine or sample-log information in text and JSON.

## Build

- Accept an explicit input path and output format.
- Handle missing files and malformed input with documented exit codes.
- Include sample data without personal information.
- Add a dry-run option if your tool changes anything.

## Demonstrate

- Pass an invalid path and verify a useful error.
- Compare text and JSON output for the same sample.
- Run it from a directory other than the repository root.

## Deliver

A README, sample input/output, source, and one bug investigation.

## Clean up

Remove generated reports and any disposable files. No cloud resources are needed.

## Explain this tradeoff

How would the script behave with a large input or a non-UTF-8 file?

[Resources](../resources/foundations.md) · [All projects](README.md) · [Architecture decision template](../templates/architecture-decision.md)
