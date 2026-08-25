# Google Autocomplete API — examples

Raw Google autocomplete suggestions for one seed query, with Google's relevance score.

**Live page, full schema & pricing → [quanticdata.io/collectors/google-autocomplete-api/](https://quanticdata.io/collectors/google-autocomplete-api/)**

One call to Google's autocomplete endpoint for a seed query: every suggestion with its relevance score and type, exactly as the search box would offer them. For bulk expansion of a seed (a–z, questions, prepositions, comparisons) use the keyword_ideas collector instead — this is the single-seed primitive.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/google_autocomplete/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "web scraping", "country": "us", "lang": "en", "max_results": 10}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `query` (string, required) — The partial query to complete, e.g. "proxy ser".
- `country` (string) — ISO 3166-1 alpha-2 code — proxy exit geo and Google locale (gl). Omit for the default pool.
- `lang` (string) — Interface language (hl), e.g. en, it, de.
- `max_results` (integer) — How many suggestions to deliver at most (1–20). You pay only for delivered suggestions.

## Output — one row per suggestion

| field | type | description |
|---|---|---|
| `rank` | integer | Suggestion order as Google returns it. |
| `suggestion` | string | The suggested query. |
| `relevance` | integer | Google's relevance score, when provided. |
| `type` | string | Suggestion kind (QUERY, ENTITY…), when provided. |
| `seed` | string | The seed that produced this suggestion. |

## Pricing

**$0.0002 per delivered suggestion** ($0.2 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 10,000 suggestions — no card required.

## Links

- This collector: https://quanticdata.io/collectors/google-autocomplete-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
