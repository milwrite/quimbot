#!/usr/bin/env python3
"""DropCatch scraper (public JSON API).

Goal: collect near-term expiring/auction domains (starting with AuctionsEndingToday)
without paid services.

Outputs:
- JSONL rows with raw item payload + scrape metadata.

Usage:
  python3 sidequests/domain-expirations/dropcatch_scrape.py \
    --out sidequests/domain-expirations/data/dropcatch_ending_today.jsonl \
    --pages 20 --size 250

Notes:
- The DropCatch frontend calls https://client.dropcatch.com/Filters and /Search.
- This script only uses /Search and does not require authentication.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import time
from typing import Any, Callable, Dict, List, Optional

import requests

API_BASE = "https://client.dropcatch.com"


def iso_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def post_json(session: requests.Session, url: str, payload: dict, timeout: int = 60) -> dict:
    r = session.post(
        url,
        json=payload,
        headers={
            "accept": "application/json",
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36",
        },
        timeout=timeout,
    )
    r.raise_for_status()
    return r.json()


def iter_search_pages(
    session: requests.Session,
    *,
    search_term: str,
    filters: List[Dict[str, Any]],
    size: int,
    pages: int,
    sleep_s: float,
    sorts: Optional[List[Dict[str, Any]]] = None,
    stop_when: Optional[Callable[[List[Dict[str, Any]], List[Dict[str, Any]]], bool]] = None,
) -> List[Dict[str, Any]]:
    all_items: List[Dict[str, Any]] = []
    sorts = sorts or []

    for page in range(1, pages + 1):
        payload = {
            "searchTerm": search_term,
            "filters": filters,
            "page": page,
            "size": size,
            "cursor": {"previous": "", "next": ""},
            "sorts": sorts,
        }
        data = post_json(session, f"{API_BASE}/Search", payload)
        items = (data.get("result") or {}).get("items") or []
        if not isinstance(items, list):
            raise RuntimeError(f"Unexpected items type: {type(items)}")

        sys.stderr.write(f"page={page} items={len(items)}\n")
        sys.stderr.flush()

        all_items.extend(items)

        if stop_when and stop_when(items, all_items):
            break
        if len(items) == 0:
            break
        if sleep_s:
            time.sleep(sleep_s)

    return all_items


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--size", type=int, default=250)
    ap.add_argument("--pages", type=int, default=20)
    ap.add_argument("--sleep", type=float, default=0.2)
    ap.add_argument(
        "--mode",
        choices=["ending-today", "ending-soon"],
        default="ending-today",
        help="Which DropCatch view to scrape.",
    )
    ap.add_argument(
        "--window-days",
        type=int,
        default=3,
        help="For ending-soon: include auctions ending within the next N days (UTC).",
    )
    ap.add_argument(
        "--record-type",
        action="append",
        dest="record_types",
        help=(
            "Optional: restrict to these RecordType values (repeatable). "
            "Example: --record-type 'Pending Delete'"
        ),
    )
    ap.add_argument(
        "--with-bids",
        action="store_true",
        help="Optional: restrict to auctions that already have bids (AuctionsWithBids filter).",
    )
    args = ap.parse_args()

    # Ensure parent dir exists
    import os

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    session = requests.Session()

    filters: List[Dict[str, Any]] = []

    if args.mode == "ending-today":
        filters.append(
            {"Name": "AuctionsEndingToday", "values": [{"Value": "AuctionsEndingToday"}]}
        )

    elif args.mode == "ending-soon":
        # Strategy:
        # - Sort by ExpirationDate ascending (supported by /Search).
        # - Paginate only as far as needed to cover the requested window.
        # - Optionally restrict RecordType to avoid obviously-stale PreRelease artifacts
        #   (some PreRelease rows appear with very old expirationDate values).
        if args.with_bids:
            filters.append(
                {"Name": "AuctionsWithBids", "values": [{"Value": "AuctionsWithBids"}]}
            )

        if args.record_types:
            filters.append(
                {
                    "Name": "RecordType",
                    "values": [{"Value": v} for v in args.record_types],
                }
            )

    else:
        raise ValueError(args.mode)

    sorts: List[Dict[str, Any]] = []
    stop_when = None

    if args.mode == "ending-soon":
        sorts = [{"Field": "ExpirationDate", "Direction": "Ascending"}]
        now = dt.datetime.now(dt.timezone.utc)
        window_end = now + dt.timedelta(days=args.window_days)

        def parse_z(s: str) -> dt.datetime:
            # DropCatch returns ISO8601 with trailing 'Z'
            if s.endswith("Z"):
                s = s[:-1] + "+00:00"
            return dt.datetime.fromisoformat(s)

        def _stop_when(page_items, all_items):
            # Stop once we've started seeing future auctions, and the max ExpirationDate
            # we just saw is beyond our window.
            if not page_items:
                return True
            try:
                page_dts = [parse_z(it["expirationDate"]) for it in page_items if it.get("expirationDate")]
                max_dt = max(page_dts)
            except Exception:
                return False

            seen_future = False
            for it in all_items:
                try:
                    if parse_z(it.get("expirationDate")) >= now:
                        seen_future = True
                        break
                except Exception:
                    continue

            return seen_future and (max_dt > window_end)

        stop_when = _stop_when

    items = iter_search_pages(
        session,
        search_term="",
        filters=filters,
        size=args.size,
        pages=args.pages,
        sleep_s=args.sleep,
        sorts=sorts,
        stop_when=stop_when,
    )

    if args.mode == "ending-soon":
        # Post-filter to the requested window, and discard obviously-stale past dates.
        now = dt.datetime.now(dt.timezone.utc)
        window_end = now + dt.timedelta(days=args.window_days)

        def parse_z(s: str) -> Optional[dt.datetime]:
            if not s:
                return None
            if s.endswith("Z"):
                s = s[:-1] + "+00:00"
            try:
                return dt.datetime.fromisoformat(s)
            except ValueError:
                return None

        filtered = []
        for it in items:
            ex = parse_z(it.get("expirationDate"))
            if not ex:
                continue
            # Keep only auctions that have not ended yet.
            if ex < now:
                continue
            if ex <= window_end:
                filtered.append(it)
        items = filtered

    meta = {
        "scraped_at": iso_now(),
        "api_base": API_BASE,
        "mode": args.mode,
        "size": args.size,
        "pages": args.pages,
        "count": len(items),
        "window_days": args.window_days if args.mode == "ending-soon" else None,
        "record_types": args.record_types,
        "with_bids": bool(getattr(args, "with_bids", False)),
    }

    with open(args.out, "a", encoding="utf-8") as f:
        for it in items:
            row = {
                "_meta": meta,
                "item": it,
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    sys.stderr.write(f"wrote={len(items)} out={args.out}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
