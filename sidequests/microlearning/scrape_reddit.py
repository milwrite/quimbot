#!/usr/bin/env python3
"""Reddit scraper for microlearning pipeline.

Scrapes educational subreddits for trending posts, produces topic_record JSONL
per the schema in schemas/topic_record.schema.json.
"""
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

# --- Config ---
SUBREDDITS = [
    "todayilearned",
    "explainlikeimfive",
    "Futurology",
    "science",
    "nutrition",
    "psychology",
    "LifeProTips",
    "YouShouldKnow",
    "Showerthoughts",
    "interestingasfuck",
]

SORT_MODES = ["hot", "top"]  # scrape both hot and top (day)
LIMIT_PER_SUB = 25
MIN_UPVOTES = 500

CLIENT_ID = os.environ.get("REDDIT_CLIENT_ID", "")
CLIENT_SECRET = os.environ.get("REDDIT_CLIENT_SECRET", "")
USER_AGENT = "quimbot/1.0 (by /u/milwrite)"


def get_token():
    """Get Reddit OAuth token (installed_client grant)."""
    resp = requests.post(
        "https://www.reddit.com/api/v1/access_token",
        auth=(CLIENT_ID, CLIENT_SECRET),
        data={
            "grant_type": "https://oauth.reddit.com/grants/installed_client",
            "device_id": "DO_NOT_TRACK_THIS_DEVICE",
        },
        headers={"User-Agent": USER_AGENT},
    )
    resp.raise_for_status()
    data = resp.json()
    if "access_token" not in data:
        raise RuntimeError(f"Reddit auth failed: {data}")
    return data["access_token"]


def scrape_subreddit(token, subreddit, sort="hot", limit=25, time_filter="day"):
    """Scrape posts from a subreddit."""
    url = f"https://oauth.reddit.com/r/{subreddit}/{sort}"
    params = {"limit": limit}
    if sort == "top":
        params["t"] = time_filter

    resp = requests.get(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": USER_AGENT,
        },
        params=params,
    )
    resp.raise_for_status()
    return resp.json()["data"]["children"]


def post_to_topic_record(post_data, captured_at):
    """Convert a Reddit post to a topic_record."""
    d = post_data["data"]
    sub = d["subreddit"]
    post_id = d["id"]
    topic_id = hashlib.sha1(f"{sub}:{post_id}".encode()).hexdigest()

    created_utc = d.get("created_utc", 0)
    created_at = datetime.fromtimestamp(created_utc, tz=timezone.utc).isoformat()

    # Compute velocities
    age_hours = max((captured_at.timestamp() - created_utc) / 3600, 0.1)
    upvotes = d.get("ups", 0)
    num_comments = d.get("num_comments", 0)

    record = {
        "topic_id": f"sha1:{topic_id}",
        "source": {
            "provider": "reddit",
            "subreddit": sub,
            "post_id": post_id,
            "post_permalink": d.get("permalink", ""),
        },
        "title": d.get("title", ""),
        "url": f"https://www.reddit.com{d.get('permalink', '')}",
        "author": d.get("author", "[deleted]"),
        "created_at": created_at,
        "captured_at": captured_at.isoformat(),
        "metrics": {
            "upvotes": upvotes,
            "num_comments": num_comments,
            "comment_velocity_per_hour": round(num_comments / age_hours, 2),
            "upvote_velocity_per_hour": round(upvotes / age_hours, 2),
        },
        "keywords": [],  # could enrich later
        "entities": [],
        "risk_flags": detect_risk_flags(d),
        "microlearning_angle_candidates": [],
    }
    return record


def detect_risk_flags(post_data):
    """Basic keyword-based risk flag detection."""
    flags = []
    title = (post_data.get("title", "") + " " + post_data.get("selftext", "")).lower()

    if any(w in title for w in ["cure", "treatment", "diagnosis", "symptom", "doctor"]):
        flags.append("medical_claim")
    if any(w in title for w in ["invest", "stock", "crypto", "buy", "sell", "profit"]):
        flags.append("finance_advice")
    if any(w in title for w in ["trump", "biden", "election", "democrat", "republican", "congress"]):
        flags.append("politics")
    if post_data.get("over_18", False):
        flags.append("adult")

    return flags


def main():
    outdir = Path(__file__).parent / "data"
    outdir.mkdir(exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M")
    outfile = outdir / f"topics_{timestamp}.jsonl"

    print(f"[scraper] Authenticating with Reddit API...")
    token = get_token()
    print(f"[scraper] Auth OK")

    captured_at = datetime.now(timezone.utc)
    all_records = []
    seen_ids = set()

    for sub in SUBREDDITS:
        for sort in SORT_MODES:
            try:
                print(f"[scraper] Scraping r/{sub}/{sort}...", end=" ")
                posts = scrape_subreddit(token, sub, sort=sort, limit=LIMIT_PER_SUB)
                count = 0
                for p in posts:
                    record = post_to_topic_record(p, captured_at)
                    if record["topic_id"] in seen_ids:
                        continue
                    if record["metrics"]["upvotes"] < MIN_UPVOTES:
                        continue
                    seen_ids.add(record["topic_id"])
                    all_records.append(record)
                    count += 1
                print(f"{count} new posts (>={MIN_UPVOTES} upvotes)")
                time.sleep(1)  # rate limiting
            except Exception as e:
                print(f"ERROR: {e}")
                time.sleep(2)

    # Write JSONL
    with open(outfile, "w") as f:
        for r in all_records:
            f.write(json.dumps(r) + "\n")

    print(f"\n[scraper] Done! Wrote {len(all_records)} topic records to {outfile}")
    return outfile, all_records


if __name__ == "__main__":
    main()
