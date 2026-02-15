#!/usr/bin/env python3
"""Normalize DropCatch JSONL -> a simpler schema for downstream UI.

Input: JSONL rows produced by dropcatch_scrape.py (each line: {_meta, item}).
Output: JSONL rows (each line: normalized dict).

Example:
  python3 sidequests/domain-expirations/normalize_dropcatch.py \
    --in sidequests/domain-expirations/data/dropcatch_ending_soon_*.jsonl \
    --out sidequests/domain-expirations/data/normalized_dropcatch_ending_soon.jsonl
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import os
from typing import Any, Dict, Iterable, Optional


def parse_z(s: str) -> Optional[dt.datetime]:
    if not s:
        return None
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    try:
        return dt.datetime.fromisoformat(s)
    except ValueError:
        return None


def iter_inputs(patterns: Iterable[str]):
    for p in patterns:
        for path in sorted(glob.glob(p)):
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    yield path, json.loads(line)


def norm_row(source_path: str, row: Dict[str, Any]) -> Dict[str, Any]:
    meta = row.get("_meta") or {}
    it = row.get("item") or {}

    end_dt = parse_z(it.get("expirationDate"))
    end_iso = end_dt.isoformat().replace("+00:00", "Z") if end_dt else None
    end_ms = int(end_dt.timestamp() * 1000) if end_dt else None

    return {
        "source": "dropcatch",
        "scraped_at": meta.get("scraped_at"),
        "mode": meta.get("mode"),
        "auction_id": it.get("id"),
        "domain": it.get("name"),
        "record_type": it.get("recordType"),
        "end_time": end_iso,
        "end_time_ms": end_ms,
        "high_bid": it.get("highBid"),
        "next_valid_bid": it.get("nextValidBid"),
        "bids": it.get("numberOfBids"),
        "bidders": it.get("numberOfBidders"),
        "high_bidder": it.get("highBidder"),
        "_source_path": os.path.basename(source_path),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inputs", action="append", required=True, help="Glob/path; repeatable")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    with open(args.out, "w", encoding="utf-8") as out:
        for source_path, row in iter_inputs(args.inputs):
            out.write(json.dumps(norm_row(source_path, row), ensure_ascii=False) + "\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
