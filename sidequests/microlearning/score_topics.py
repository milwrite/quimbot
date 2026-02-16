#!/usr/bin/env python3
"""Score and rank topic records using the POC formula from scoring.md.

Base score:
  score_raw = 0.45*v_comments + 0.15*v_upvotes + 0.15*echo + 0.15*feasible + 0.10*novelty - 0.25*risk

Then apply an explicit subreddit prior/weight to reduce over-selection from
high-volume subs like r/todayilearned:
  score_final = score_raw * w_subreddit

Outputs a shortlist JSON file.
"""
import json
import sys
from pathlib import Path
from collections import Counter


# Subreddit prior weights (default 1.0). Adjust to steer diversity.
SUBREDDIT_WEIGHTS = {
    "todayilearned": 0.7,
    "explainlikeimfive": 1.0,
    "science": 1.1,
    "Futurology": 1.0,
    "technology": 1.0,
    "YouShouldKnow": 1.0,
    "LifeProTips": 1.0,
    "nutrition": 1.0,
    "psychology": 1.0,
    "interestingasfuck": 0.9,
    "Showerthoughts": 0.85,
}


def normalize(value, max_val):
    """Normalize to 0-1 range."""
    if max_val <= 0:
        return 0
    return min(value / max_val, 1.0)


def score_topics(input_file, top_n=20):
    records = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    if not records:
        print("No records to score!")
        return []

    # Compute max values for normalization
    max_comment_vel = max(r["metrics"].get("comment_velocity_per_hour", 0) for r in records) or 1
    max_upvote_vel = max(r["metrics"].get("upvote_velocity_per_hour", 0) for r in records) or 1

    # Count subreddit echoes (multiple posts = trending topic area)
    sub_counts = Counter(r["source"]["subreddit"] for r in records)

    scored = []
    for r in records:
        m = r["metrics"]

        # Component scores (0-1)
        v_comments = normalize(m.get("comment_velocity_per_hour", 0), max_comment_vel)
        v_upvotes = normalize(m.get("upvote_velocity_per_hour", 0), max_upvote_vel)

        # Echo: more posts from same sub = trending area
        echo = normalize(sub_counts[r["source"]["subreddit"]], max(sub_counts.values()))

        # Feasibility heuristic: shorter titles tend to be more explainable
        # Also boost certain "learning" subreddits
        learning_subs = {"todayilearned", "explainlikeimfive", "YouShouldKnow", "LifeProTips"}
        feasible = 0.7 if r["source"]["subreddit"] in learning_subs else 0.4
        if len(r["title"]) < 100:
            feasible += 0.2

        # Novelty: 1.0 for all (no history yet)
        novelty = 1.0

        # Risk penalty
        risk = 0.0
        hard_blocks = {"adult", "violence", "self_harm", "hate"}
        soft_flags = {"medical_claim", "finance_advice", "politics"}
        for flag in r.get("risk_flags", []):
            if flag in hard_blocks:
                risk = 1.0
                break
            if flag in soft_flags:
                risk = max(risk, 0.5)

        # Base score (before subreddit prior)
        score_raw = (
            0.45 * v_comments
            + 0.15 * v_upvotes
            + 0.15 * echo
            + 0.15 * feasible
            + 0.10 * novelty
            - 0.25 * risk
        )

        subreddit = r["source"]["subreddit"]
        w_sub = SUBREDDIT_WEIGHTS.get(subreddit, 1.0)
        score = score_raw * w_sub

        scored.append({
            "topic_id": r["topic_id"],
            "title": r["title"],
            "subreddit": subreddit,
            "url": r["url"],
            "score": round(score, 4),
            "score_raw": round(score_raw, 4),
            "components": {
                "v_comments": round(v_comments, 3),
                "v_upvotes": round(v_upvotes, 3),
                "echo": round(echo, 3),
                "feasible": round(feasible, 3),
                "novelty": round(novelty, 3),
                "risk": round(risk, 3),
                "w_subreddit": w_sub,
            },
            "metrics": m,
            "risk_flags": r.get("risk_flags", []),
        })

    # Sort by score descending
    scored.sort(key=lambda x: x["score"], reverse=True)

    return scored[:top_n]


def main():
    input_file = sys.argv[1] if len(sys.argv) > 1 else None
    if not input_file:
        # Find latest topics file
        data_dir = Path(__file__).parent / "data"
        files = sorted(data_dir.glob("topics_*.jsonl"))
        if not files:
            print("No topics files found!")
            sys.exit(1)
        input_file = str(files[-1])

    print(f"[scorer] Scoring topics from {input_file}")
    shortlist = score_topics(input_file, top_n=15)

    # Write shortlist
    outdir = Path(input_file).parent
    outfile = outdir / input_file.replace("topics_", "shortlist_").replace(".jsonl", ".json").split("/")[-1]
    with open(outfile, "w") as f:
        json.dump({"shortlist": shortlist, "source_file": str(input_file), "count": len(shortlist)}, f, indent=2)

    print(f"[scorer] Top 15 shortlisted → {outfile}")
    print()
    for i, s in enumerate(shortlist, 1):
        flags = f" ⚠️{','.join(s['risk_flags'])}" if s['risk_flags'] else ""
        print(f"  {i:2d}. [{s['score']:.3f}] r/{s['subreddit']}: {s['title'][:65]}{flags}")

    return outfile, shortlist


if __name__ == "__main__":
    main()
