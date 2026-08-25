"""Minimal Google Autocomplete API call — one typed row per suggestion.

Docs & schema: https://quanticdata.io/collectors/google-autocomplete-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/google_autocomplete/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "query": "web scraping",
        "country": "us",
        "lang": "en",
        "max_results": 10
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("suggestion"), row.get("relevance"), row.get("type"))
print(f"{len(data['results'])} suggestions, cost ${data['cost']}")
