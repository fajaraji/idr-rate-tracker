# IDR Exchange Rate Tracker

Daily USD/IDR observations from Frankfurter, appended to a CSV by Python and recorded in Git history with GitHub Actions.

## Explore the implementation

Each row carries the exchange-rate date returned by the API and the time the script fetched it. Multiple runs can therefore record the same rate date.

- [Fetch and append one observation](main.py)
- [Daily schedule and manual trigger](.github/workflows/daily_run.yml)
- [Python dependencies](requirements.txt)

## Run one observation

```bash
python -m pip install -r requirements.txt
python main.py
```

Open [the history](data/exchange_rates.csv) and inspect the last row. The scheduled workflow requests a run at 00:00 UTC (07:00 WIB). On weekends or a manual rerun, compare the API date and fetch timestamp before counting distinct trading days.
