#!/usr/bin/env python3
"""Check catalog URLs. Blocked/transient responses need manual review, not blind deletion."""
import argparse
import concurrent.futures
import datetime
import json
from pathlib import Path
import ssl
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
REVIEW_CODES = {401, 403, 406, 408, 409, 425, 429}


def check(row):
    url = row['url']
    result = {'id': row['id'], 'url': url}
    # Use the platform trust store, including Homebrew/macOS Python installations.
    ca = Path('/etc/ssl/cert.pem')
    context = ssl.create_default_context(cafile=str(ca) if ca.exists() else None)
    request = urllib.request.Request(url, headers={'User-Agent': 'CloudDevOpsLearningHub-LinkCheck/1.0 (+https://github.com/aniketsingh1023/cloud-devops-zero-to-100)'})
    try:
        with urllib.request.urlopen(request, timeout=20, context=context) as response:
            result.update(status=response.status, final_url=response.url, outcome='ok')
            # Only verify reachability; no articles or binaries are downloaded.
    except urllib.error.HTTPError as error:
        result.update(status=error.code, outcome='review' if 300 <= error.code < 400 or error.code in REVIEW_CODES or error.code >= 500 else 'broken', detail=str(error))
    except (OSError, urllib.error.URLError, TimeoutError) as error:
        result.update(status=None, outcome='review', detail=str(error))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='link-report.json')
    parser.add_argument('--workers', type=int, default=6)
    parser.add_argument('--strict', action='store_true', help='Also fail for responses requiring manual review')
    args = parser.parse_args()
    if not 1 <= args.workers <= 12:
        parser.error('--workers must be between 1 and 12')
    rows = json.loads((ROOT / 'data/resources.json').read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(check, rows))
    report = {'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'note': 'Reachability only. HTTP 200 does not establish editorial quality, free access or lack of a soft 404.', 'results': results}
    Path(args.output).write_text(json.dumps(report, indent=2) + '\n')
    for result in results:
        if result['outcome'] != 'ok':
            print(f'{result["outcome"]}: {result["status"]} {result["url"]}')
    counts = {state: sum(r['outcome'] == state for r in results) for state in ('ok', 'review', 'broken')}
    print(f'{counts}; report: {args.output}')
    raise SystemExit(1 if counts['broken'] or (args.strict and counts['review']) else 0)


if __name__ == '__main__':
    main()
