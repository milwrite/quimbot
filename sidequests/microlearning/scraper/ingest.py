#!/usr/bin/env python3
"""Reddit trend ingester for microlearning pipeline.
Scrapes target subreddits and outputs normalized JSONL topic records.
Uses public JSON endpoints (no OAuth required).
"""

import json
import hashlib
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONFIG_PATH = SCRIPT_DIR / "config.json"
DATA_DIR = SCRIPT_DIR / "data"
DELTA_PATH = DATA_DIR / "delta.json"

USER_AGENT = "Mozilla/5.0 (Microlearning Bot 1.0)"

RISK_KEYWORDS = {
    "medical": ["cure", "treatment", "cancer", "disease", "drug", "fda", "clinical trial", "vaccine", "diagnosis"],
    "finance": ["stock", "crypto", "invest", "portfolio", "trading", "bitcoin", "ethereum", "hedge fund"],
    "politics": ["election", "democrat", "republican", "trump", "biden", "congress", "senate", "legislation"],
    "adult": ["nsfw", "porn", "xxx", "onlyfans"],
}


def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)


def load_delta():
    if DELTA_PATH.exists():
        with open(DELTA_PATH) as f:
            return json.load(f)
    return {}


def save_delta(delta):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DELTA_PATH, "w") as f:
        json.dump(delta, f, indent=2)


def fetch_subreddit(sub, sort="hot", limit=10, time_filter="day"):
    """Fetch posts from a subreddit using public JSON API."""
    url = f"https://www.reddit.com/r/{sub}/{sort}.json?limit={limit}&t={time_filter}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            return data.get("data", {}).get("children", [])
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        print(f"  ⚠ Error fetching r/{sub}/{sort}: {e}")
        return []


def make_topic_id(subreddit, post_id):
    return hashlib.sha1(f"{subreddit}:{post_id}".encode()).hexdigest()[:12]


def detect_risk_flags(title, selftext=""):
    combined = (title + " " + selftext).lower()
    flags = []
    for category, keywords in RISK_KEYWORDS.items():
        if any(kw in combined for kw in keywords):
            flags.append(category)
    return flags


def extract_keywords(title):
    """Basic keyword extraction from title."""
    stop = {"the", "a", "an", "is", "are", "was", "were", "be", "been", "being",
            "have", "has", "had", "do", "does", "did", "will", "would", "could",
            "should", "may", "might", "shall", "can", "to", "of", "in", "for",
            "on", "with", "at", "by", "from", "as", "into", "about", "like",
            "through", "after", "over", "between", "out", "against", "during",
            "without", "before", "under", "around", "among", "and", "but", "or",
            "so", "yet", "both", "either", "neither", "not", "only", "own",
            "same", "than", "too", "very", "just", "that", "this", "it", "i",
            "my", "your", "his", "her", "its", "our", "their", "what", "which",
            "who", "whom", "how", "when", "where", "why", "all", "each", "every",
            "no", "any", "few", "more", "most", "other", "some", "such"}
    words = title.lower().split()
    clean = [w.strip(".,!?()[]{}\"'") for w in words]
    return [w for w in clean if len(w) > 2 and w not in stop][:8]


def process_post(post_data, subreddit, delta):
    """Convert a Reddit post to a normalized topic record."""
    d = post_data.get("data", {})
    post_id = d.get("id", "")
    topic_id = make_topic_id(subreddit, post_id)

    score = d.get("score", 0)
    num_comments = d.get("num_comments", 0)
    created_utc = d.get("created_utc", 0)

    # Velocity: compare with previous scrape
    prev = delta.get(topic_id, {})
    prev_score = prev.get("score", 0)
    prev_comments = prev.get("num_comments", 0)
    velocity = (score - prev_score) + (num_comments - prev_comments) * 2

    title = d.get("title", "")

    return {
        "topic_id": topic_id,
        "subreddit": subreddit,
        "post_id": post_id,
        "post_title": title,
        "post_url": f"https://reddit.com{d.get('permalink', '')}",
        "score": score,
        "num_comments": num_comments,
        "created_utc": created_utc,
        "velocity": velocity,
        "upvote_ratio": d.get("upvote_ratio", 0),
        "keywords": extract_keywords(title),
        "risk_flags": detect_risk_flags(title, d.get("selftext", "")),
        "scraped_at": datetime.now(timezone.utc).isoformat(),
    }


def run_ingest():
    config = load_config()
    delta = load_delta()
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H")
    outpath = DATA_DIR / f"topics-{timestamp}.jsonl"

    all_records = []
    new_delta = {}

    for sub in config["subreddits"]:
        for sort in config["sort_modes"]:
            print(f"  Fetching r/{sub}/{sort}...")
            posts = fetch_subreddit(sub, sort, config["posts_per_sub"], config["time_filter"])
            for post in posts:
                record = process_post(post, sub, delta)
                all_records.append(record)
                new_delta[record["topic_id"]] = {
                    "score": record["score"],
                    "num_comments": record["num_comments"],
                }
            time.sleep(1.0)  # Rate limit

    # Deduplicate by topic_id
    seen = set()
    unique = []
    for r in all_records:
        if r["topic_id"] not in seen:
            seen.add(r["topic_id"])
            unique.append(r)

    # Write JSONL
    with open(outpath, "w") as f:
        for r in unique:
            f.write(json.dumps(r) + "\n")

    save_delta(new_delta)

    print(f"✅ Wrote {len(unique)} topics to {outpath}")
    return outpath, unique


if __name__ == "__main__":
    run_ingest()
