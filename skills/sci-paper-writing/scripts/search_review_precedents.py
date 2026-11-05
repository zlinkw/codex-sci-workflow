"""Bounded public ReviewSearch retrieval; never uploads manuscript files or runs AI."""
from __future__ import annotations
import argparse
import json
import sys
import urllib.request
import urllib.error

ENDPOINT = 'https://yjoonjang-reviewsearch.hf.space/api/search'


def payload(query, top_k=3, year_min=None, year_max=None, accepted_only=False):
    if not isinstance(query, str) or not query.strip() or len(query) > 500 or '\x00' in query:
        raise ValueError('Use a short anonymized English concern query, at most 500 characters.')
    if not isinstance(top_k, int) or isinstance(top_k, bool) or not 1 <= top_k <= 5:
        raise ValueError('top-k must be 1–5.')
    for year in (year_min, year_max):
        if year is not None and (not isinstance(year, int) or isinstance(year, bool) or not 1900 <= year <= 2100):
            raise ValueError('Invalid year bound.')
    if year_min is not None and year_max is not None and year_min > year_max:
        raise ValueError('Year bounds are reversed.')
    result = dict(query=query.strip(), top_k=top_k, accepted_only=bool(accepted_only))
    if year_min is not None: result['year_min'] = year_min
    if year_max is not None: result['year_max'] = year_max
    return result


def search(data, timeout=30):
    request = urllib.request.Request(ENDPOINT, data=json.dumps(data).encode('utf-8'),
                                     headers={'Content-Type': 'application/json', 'User-Agent': 'Codex-Public-ReviewSearch/1.0'})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read(2 * 1024 * 1024 + 1)
    if len(raw) > 2 * 1024 * 1024: raise ValueError('ReviewSearch response exceeded the bounded limit.')
    result = json.loads(raw.decode('utf-8'))
    if not isinstance(result, dict) or not isinstance(result.get('results'), list):
        raise ValueError('ReviewSearch returned an unexpected schema; no examples were accepted.')
    if len(result['results']) > data['top_k'] or any(not isinstance(row, dict) for row in result['results']):
        raise ValueError('ReviewSearch returned invalid or excessive results.')
    return {'source': ENDPOINT, 'data_attribution': 'OpenReview public reviews, CC-BY-4.0; indexed by ReviewSearch',
            'original_links_verified': False, 'count': len(result['results']), 'results': result['results']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query', required=True)
    parser.add_argument('--top-k', type=int, default=3)
    parser.add_argument('--year-min', type=int)
    parser.add_argument('--year-max', type=int)
    parser.add_argument('--accepted-only', action='store_true')
    args = parser.parse_args()
    result = search(payload(args.query, args.top_k, args.year_min, args.year_max, args.accepted_only))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try: main()
    except (ValueError, OSError, urllib.error.URLError) as error:
        print('ReviewSearch unavailable: ' + str(error) + '. No retry, fabricated examples or experiment execution.', file=sys.stderr)
        sys.exit(1)
