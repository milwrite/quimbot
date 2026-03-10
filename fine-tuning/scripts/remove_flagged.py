#!/usr/bin/env python3
"""Remove flagged degenerate entries from superset3_merged.jsonl by line number."""
import json
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
INPUT = DATA_DIR / "toefl_superset3_merged_20260227_0701.jsonl"
FLAGGED = DATA_DIR / "superset3_flagged_short_lines.txt"
OUTPUT = DATA_DIR / "superset3_cleaned.jsonl"

# Read flagged line numbers (1-indexed)
flagged_lines = set()
for tok in FLAGGED.read_text().strip().split(","):
    flagged_lines.add(int(tok.strip()))

kept = 0
removed = 0
with open(INPUT) as fin, open(OUTPUT, "w") as fout:
    for i, line in enumerate(fin, 1):
        if i in flagged_lines:
            removed += 1
            continue
        fout.write(line)
        kept += 1

print(f"Removed {removed} flagged entries, kept {kept}. Output: {OUTPUT}")
