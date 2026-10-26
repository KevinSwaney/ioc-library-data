# IOC Library Data

Structured indicators of compromise, in JSON, for defenders to pull into their own tools.

## Format

Each entry in `data/iocs.json` has:
- `type`: domain, ip, url, hash, or file
- `value`: the indicator itself
- `date_added`: YYYY-MM-DD
- `source`: where it was published, or "example" for the sample entries
- `confidence`: high, medium, or low
- `verified`: true only when the indicator was corroborated from a primary source. Unverified claims stay marked unverified, never presented as confirmed.
- `context`: what it was seen with, in plain language

## Rules

- Public indicators only. No private, client, or employer data.
- Never present an unverified indicator as confirmed. If in doubt, mark it low confidence and unverified.
- Check an indicator before blocking on it alone. One indicator is a lead, not a verdict.
- The sample entries in `data/iocs.json` are format examples only, not real indicators. Replace them with real, sourced entries before using this as a live feed.

## Validate

Run: `python3 validate.py`
