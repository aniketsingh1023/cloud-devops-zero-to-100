#!/usr/bin/env python3
"""Validate, render and search the resource catalog using only Python's standard library."""
import argparse
import difflib
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {'id', 'title', 'url', 'category', 'level', 'type', 'access', 'why', 'practice'}


def load():
    rows = json.loads((ROOT / 'data/resources.json').read_text())
    categories = json.loads((ROOT / 'data/categories.json').read_text())
    ids, urls = set(), set()
    for row in rows:
        assert set(row) == FIELDS, f'Unexpected fields: {row}'
        assert all(isinstance(v, str) and v.strip() for v in row.values()), row
        assert row['id'] not in ids, f'Duplicate id: {row["id"]}'
        assert row['url'].rstrip('/') not in urls, f'Duplicate URL: {row["url"]}'
        assert row['category'] in categories, f'Unknown category: {row["category"]}'
        assert row['level'] in {'Beginner', 'Intermediate', 'Advanced'}, row
        parsed = urlparse(row['url'])
        assert parsed.scheme == 'https' and parsed.netloc, f'Invalid URL: {row["url"]}'
        assert not any(c in row['title'] for c in '|[]\n'), row
        ids.add(row['id'])
        urls.add(row['url'].rstrip('/'))
    assert rows, 'Empty catalog'
    assert set(categories) == {r['category'] for r in rows}, 'Empty category'
    return rows, categories


def pages(rows, categories):
    index = ['# Resource library', '', f'**{len(rows)} curated resources across {len(categories)} categories.** Each has an original annotation and a practical next step.', '',
             'Labels describe the linked resource, not a guarantee of permanent access. “Free” reading does not cover cloud usage, optional products, certification exams or every linked sub-resource.', '',
             '| Category | Resources |', '|---|---:|']
    output = {}
    for key, meta in categories.items():
        entries = [r for r in rows if r['category'] == key]
        index.append(f'| [{meta["title"]}]({key}.md) | {len(entries)} |')
        lines = [f'# {meta["title"]}', '', meta['intro'], '', '[All categories](README.md) · [Roadmap](../roadmap/100-days.md) · [Start here](../START-HERE.md)', '']
        for row in entries:
            lines.extend([f'## {row["title"]}', '', f'[{row["type"]} →]({row["url"]}) · **{row["level"]}** · **Access:** {row["access"]}', '', row['why'], '', f'**Try this:** {row["practice"]}', ''])
        lines.extend(['---', '', 'Generated from [the resource catalog](../data/resources.json). Suggest edits through [the contribution guide](../CONTRIBUTING.md).', ''])
        output[f'resources/{key}.md'] = '\n'.join(lines)
    index.extend(['', '## Search locally', '', 'Requires Python 3.11+; no packages or API keys.', '', '```bash', 'python3 scripts/catalog.py search kubernetes', 'python3 scripts/catalog.py search "cost" --level Beginner', 'python3 scripts/catalog.py search --category papers', '```', '',
                  'The catalog is in [JSON](../data/resources.json). Category pages are generated so descriptions stay consistent. See [maintenance instructions](../MAINTENANCE.md).', ''])
    output['resources/README.md'] = '\n'.join(index)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('build')
    sub.add_parser('check')
    search = sub.add_parser('search')
    search.add_argument('query', nargs='?', default='')
    search.add_argument('--category')
    search.add_argument('--level', choices=['Beginner', 'Intermediate', 'Advanced'])
    args = parser.parse_args()
    rows, categories = load()
    if args.command == 'search':
        if args.category and args.category not in categories:
            parser.error(f'Unknown category. Choose: {", ".join(categories)}')
        found = [r for r in rows if args.query.casefold() in ' '.join(r.values()).casefold()
                 and (not args.category or args.category == r['category'])
                 and (not args.level or args.level == r['level'])]
        for row in found:
            print(f'{row["title"]} [{row["level"]}; {row["access"]}]\n  {row["url"]}\n  Try: {row["practice"]}')
        print(f'\n{len(found)} result(s).')
        return
    stale = []
    for relative, expected in pages(rows, categories).items():
        path = ROOT / relative
        if args.command == 'build':
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected)
        elif not path.exists() or path.read_text() != expected:
            stale.append(relative)
            print(''.join(difflib.unified_diff(path.read_text().splitlines(True) if path.exists() else [], expected.splitlines(True), fromfile=relative, tofile='generated')))
    if stale:
        parser.exit(1, 'Run python3 scripts/catalog.py build; stale pages: ' + ', '.join(stale) + '\n')
    print(f'{len(rows)} resources; {len(categories)} categories; generated pages {"written" if args.command == "build" else "current"}.')


if __name__ == '__main__':
    main()
