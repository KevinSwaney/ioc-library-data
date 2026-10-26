#!/usr/bin/env python3
"""Validate data/iocs.json entries against the required schema."""
import json, sys
REQUIRED = {"type", "value", "date_added", "source", "confidence", "verified", "context"}
TYPES = {"domain", "ip", "url", "hash", "file"}
CONF = {"high", "medium", "low"}
with open("data/iocs.json", encoding="utf-8") as f:
    data = json.load(f)
assert isinstance(data, list), "top level must be a list"
for i, e in enumerate(data):
    assert REQUIRED <= set(e), f"entry {i} missing fields"
    assert e["type"] in TYPES, f"entry {i} bad type"
    assert e["confidence"] in CONF, f"entry {i} bad confidence"
    assert isinstance(e["verified"], bool), f"entry {i} verified must be boolean"
print(f"OK: {len(data)} entries validated")
