#!/usr/bin/env python3
"""Propose microlearning candidates from scraped Reddit topics.
Reads latest JSONL, scores topics, and outputs candidate records
with hooks, scripts, and production notes.
"""

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR / "data"
CANDIDATES_DIR = SCRIPT_DIR.parent / "candidates"


def load_latest_topics():
    """Load the most recent topics JSONL file."""
    jsonl_files = sorted(DATA_DIR.glob("topics-*.jsonl"), reverse=True)
    if not jsonl_files:
        print("❌ No topic files found. Run ingest.py first.")
        sys.exit(1)

    records = []
    with open(jsonl_files[0]) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    print(f"📂 Loaded {len(records)} topics from {jsonl_files[0].name}")
    return records


def load_existing_candidates():
    """Load IDs of previously proposed candidates to avoid repeats."""
    CANDIDATES_DIR.mkdir(parents=True, exist_ok=True)
    existing = set()
    for f in CANDIDATES_DIR.glob("*.json"):
        try:
            with open(f) as fh:
                data = json.load(fh)
                if isinstance(data, list):
                    for item in data:
                        existing.add(item.get("topic_id", ""))
                elif isinstance(data, dict):
                    existing.add(data.get("topic_id", ""))
        except (json.JSONDecodeError, KeyError):
            pass
    return existing


SUBREDDIT_WEIGHTS = {
    "todayilearned": 0.7,
    "explainlikeimfive": 1.0,
    "science": 1.1,
    "Futurology": 1.1,
    "technology": 1.0,
    "Artificial": 1.1,
    "MachineLearning": 1.1,
    "datascience": 1.0,
    "investing": 0.9,
    "personalfinance": 0.9,
    "cscareerquestions": 0.9,
    "productivity": 1.0,
    "nutrition": 1.0,
    "space": 1.1,
    "Entrepreneur": 0.9,
}


def score_topic(record):
    """Compute a trendiness score for ranking."""
    score = 0

    # Velocity-weighted engagement
    score += record.get("velocity", 0) * 1.5

    # Comment-heavy posts are better for microlearning
    score += record.get("num_comments", 0) * 0.3

    # Upvote ratio (quality signal)
    score += record.get("upvote_ratio", 0) * 20

    # Base engagement
    score += min(record.get("score", 0) * 0.1, 50)  # Cap base score contribution

    # Risk penalty
    risk_flags = record.get("risk_flags", [])
    score -= len(risk_flags) * 15

    # Title length feasibility (20-80 chars is ideal for hooks)
    title_len = len(record.get("post_title", ""))
    if 20 <= title_len <= 80:
        score += 10
    elif title_len > 150:
        score -= 5

    # Subreddit weight (reduce TIL bias, boost niche subs)
    sub = record.get("subreddit", "")
    weight = SUBREDDIT_WEIGHTS.get(sub, 1.0)
    score *= weight

    return round(score, 2)


def generate_hook(record):
    """Generate a microlearning hook from the topic."""
    title = record.get("post_title", "")
    sub = record.get("subreddit", "")

    # Simple hook templates
    hooks = [
        f"Did you know? {title[:60]}...",
        f"Here's something trending in r/{sub}: {title[:50]}",
        f"Quick learn: {title[:70]}",
    ]
    return hooks[0]  # Will be replaced by LLM later


def generate_script_outline(record):
    """Generate a 20-40 second script outline."""
    title = record.get("post_title", "")
    keywords = record.get("keywords", [])

    return {
        "duration_target": "30s",
        "hook": f"[0-5s] Attention grabber about: {title[:50]}",
        "context": f"[5-15s] Why this matters: trending topic with {record.get('num_comments', 0)} comments",
        "key_insight": f"[15-25s] The main takeaway involving: {', '.join(keywords[:3])}",
        "cta": "[25-30s] What you can do with this knowledge",
    }


def propose_candidates(records, count=3):
    """Score, rank, and propose top candidates."""
    existing = load_existing_candidates()

    # Filter out already-proposed topics
    fresh = [r for r in records if r["topic_id"] not in existing]
    if not fresh:
        print("⚠ All topics already proposed. Run a new scrape.")
        return []

    # Score and sort
    for r in fresh:
        r["trendiness_score"] = score_topic(r)

    ranked = sorted(fresh, key=lambda x: x["trendiness_score"], reverse=True)

    # Take top N
    candidates = []
    for r in ranked[:count]:
        candidate = {
            "topic_id": r["topic_id"],
            "subreddit": r["subreddit"],
            "post_title": r["post_title"],
            "post_url": r["post_url"],
            "score": r["score"],
            "num_comments": r["num_comments"],
            "velocity": r["velocity"],
            "trendiness_score": r["trendiness_score"],
            "keywords": r["keywords"],
            "risk_flags": r["risk_flags"],
            "hook": generate_hook(r),
            "script_outline": generate_script_outline(r),
            "proposed_at": datetime.now(timezone.utc).isoformat(),
            "status": "proposed",
        }
        candidates.append(candidate)

    return candidates


def save_candidates(candidates):
    """Save proposed candidates to file."""
    CANDIDATES_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d-%H%M")
    outpath = CANDIDATES_DIR / f"batch-{timestamp}.json"

    with open(outpath, "w") as f:
        json.dump(candidates, f, indent=2)

    print(f"✅ Proposed {len(candidates)} candidates → {outpath}")
    return outpath


def main():
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    records = load_latest_topics()
    candidates = propose_candidates(records, count)
    if candidates:
        save_candidates(candidates)
        for i, c in enumerate(candidates, 1):
            print(f"\n--- Candidate {i} ---")
            print(f"  📌 {c['post_title'][:80]}")
            print(f"  📊 Score: {c['trendiness_score']} | r/{c['subreddit']}")
            print(f"  🎣 Hook: {c['hook'][:80]}")
            print(f"  🔗 {c['post_url']}")


if __name__ == "__main__":
    main()
