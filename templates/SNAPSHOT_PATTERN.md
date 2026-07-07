# The daily snapshot pattern (backbone 3a)

Every data-driven repo uses this exact shape. Copy, rename, done.

## Files
```
scripts/refresh.py          # fetch → normalize → write
data/latest.json            # current view (front-end reads this)
data/history/YYYY-MM-DD.json# one snapshot per day, append-only forever
.github/workflows/refresh.yml
```

## refresh.py contract
```python
#!/usr/bin/env python3
import json, datetime, os, urllib.request

def fetch():
    # ... free API calls; keys via os.environ.get("X_API_KEY") — MUST degrade
    # gracefully (keep yesterday's latest.json) if a key is missing/API down
    return {"fetched_at": datetime.datetime.utcnow().isoformat() + "Z", "series": {}}

data = fetch()
os.makedirs("data/history", exist_ok=True)
json.dump(data, open("data/latest.json", "w"), indent=2)
json.dump(data, open(f"data/history/{datetime.date.today()}.json", "w"), indent=2)
```

## refresh.yml contract
```yaml
name: Daily refresh
on:
  schedule:
    - cron: "0 8 * * *"   # SEE CRON STAGGER below — each repo has its slot
  workflow_dispatch: {}
permissions:
  contents: write
jobs:
  refresh:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: python scripts/refresh.py
        env:
          CENSUS_API_KEY: ${{ secrets.CENSUS_API_KEY }}
          FRED_API_KEY: ${{ secrets.FRED_API_KEY }}
      - run: |
          git config user.name "snapshot-bot"
          git config user.email "actions@github.com"
          git add data/
          git diff --cached --quiet || git commit -m "data: daily snapshot $(date -u +%F) [skip ci]"
          git push
```

## Cron stagger (UTC) — backbone 3b
| Slot | Repo | Purpose |
|---|---|---|
| 08:00 | us-consumer-pulse | FRED/Census refresh |
| 08:30 | bharat-consumer-pulse | monthly-cadence India data (runs daily, fetches when stale) |
| 09:00 | job-search-pipeline | scrapers (existing) + new sources |
| 10:00 | shubham-safaya.github.io | portfolio stats strip (GitHub/PyPI/RSS) |
| 10:30 | daily-engineering-log | auto-stub append |
| 10:45 | mission-control | daily email ASSEMBLY (writes data/today/) |
| 11:00 | mission-control | daily email DISPATCH (6:00 AM Central during DST) |

DST note: `0 11 * * *` = 6:00 AM Central in summer, **5:00 AM after the
November change**. To keep 6:00 AM year-round, switch to `0 12 * * *` in
November (both lines are present, one commented, in each workflow).

## Front-end contract
Render `data/latest.json` for the current view; glob `data/history/*.json`
(via the GitHub contents API or a build-time manifest) for trend charts.
