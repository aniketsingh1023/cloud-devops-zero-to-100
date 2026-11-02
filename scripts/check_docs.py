#!/usr/bin/env python3
"""Check relative Markdown targets/fragments and the complete 100-day sequence."""
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def anchors(path):
    if path.suffix.lower() != '.md':
        return set()
    text = path.read_text()
    found, counts = set(), {}
    for title in re.findall(r'^#{1,6}\s+(.+?)[ \t]*#*[ \t]*$', text, re.M):
        title = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', title)
        slug = ''.join(c for c in title.lower() if c in ' -_' or unicodedata.category(c)[0] in 'LN').replace(' ', '-')
        count = counts.get(slug, 0)
        found.add(f'{slug}-{count}' if count else slug)
        counts[slug] = count + 1
    found.update(re.findall(r'\bid=["\']([^"\']+)', text))
    return found


def main():
    errors, checked = [], 0
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        text = re.sub(r'```.*?```', '', path.read_text(), flags=re.S)
        # Inline Markdown links/images and the simple HTML asset src used in the README.
        links = re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', text)
        links += re.findall(r'<img\s[^>]*src="([^"]+)"', text)
        for raw in links:
            url = raw.strip().strip('<>')
            parsed = urlsplit(url)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            checked += 1
            if not target.is_relative_to(ROOT):
                errors.append(f'{path.relative_to(ROOT)}: target escapes repository: {url}')
            elif not target.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing target: {url}')
            elif parsed.fragment and unquote(parsed.fragment) not in anchors(target):
                errors.append(f'{path.relative_to(ROOT)}: missing heading: {url}')
    roadmap = (ROOT / 'roadmap/100-days.md').read_text()
    days = [int(day) for day in re.findall(r'\*\*Day (\d+) —', roadmap)]
    if days != list(range(1, 101)):
        errors.append('Roadmap must contain days 1–100 exactly once, in order')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'{checked} local links/fragments checked; all 100 roadmap days present.')


if __name__ == '__main__':
    main()
