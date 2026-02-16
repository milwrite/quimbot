#!/usr/bin/env python3
"""Generate content packets from shortlisted topics.

Reads a shortlist JSON, produces content_packet JSON files with
script outlines for 20-40 second microlearning videos.
"""
import json
import sys
import os
from pathlib import Path
from datetime import datetime, timezone

import requests

OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY", "")
MODEL = "google/gemini-2.5-flash-lite"


def generate_script(topic, model=MODEL):
    """Use LLM to generate a microlearning video script."""
    prompt = f"""You are a microlearning content creator for Instagram Reels/TikTok.

Given this trending topic from Reddit, create a 20-40 second video script.

Topic: {topic['title']}
Subreddit: r/{topic['subreddit']}
Upvotes: {topic['metrics']['upvotes']:,}
Comments: {topic['metrics']['num_comments']}

Requirements:
1. Hook (first 3 seconds) — grab attention immediately
2. Core fact (10-20 seconds) — the surprising/interesting thing, explained simply
3. Kicker (5-10 seconds) — a twist, deeper fact, or call to think
4. Total speaking time: 20-40 seconds max
5. Use simple language (8th grade reading level)
6. Include 1-2 "microlearning angles" — what specifically the viewer learns

Output as JSON:
{{
  "hook": "opening line (attention grabber)",
  "core_script": "main explanation (2-4 sentences)",
  "kicker": "closing twist or deeper fact",
  "estimated_seconds": 25,
  "microlearning_angles": ["angle 1", "angle 2"],
  "visual_suggestions": ["suggestion for B-roll or graphics"],
  "hashtags": ["#tag1", "#tag2", "#tag3"]
}}

Return ONLY the JSON, no markdown fencing."""

    resp = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500,
            "temperature": 0.7,
        },
    )
    resp.raise_for_status()
    content = resp.json()["choices"][0]["message"]["content"].strip()

    # Try to parse JSON from response
    # Strip markdown fencing if present
    if content.startswith("```"):
        content = content.split("\n", 1)[1]
        if content.endswith("```"):
            content = content[:-3]
        elif "```" in content:
            content = content[:content.rindex("```")]

    return json.loads(content)


def main():
    # Find latest shortlist
    data_dir = Path(__file__).parent / "data"
    shortlist_files = sorted(data_dir.glob("shortlist_*.json"))
    if not shortlist_files:
        print("No shortlist files found!")
        sys.exit(1)

    shortlist_file = shortlist_files[-1]
    print(f"[content] Loading shortlist: {shortlist_file}")

    with open(shortlist_file) as f:
        data = json.load(f)

    topics = data["shortlist"][:5]  # Top 5 only
    print(f"[content] Generating content packets for top {len(topics)} topics...\n")

    packets = []
    for i, topic in enumerate(topics, 1):
        print(f"  {i}. Generating for: {topic['title'][:60]}...")
        try:
            script = generate_script(topic)
            packet = {
                "packet_id": f"pkt_{topic['topic_id'].replace('sha1:', '')[:12]}",
                "topic_id": topic["topic_id"],
                "title": topic["title"],
                "subreddit": topic["subreddit"],
                "source_url": topic["url"],
                "score": topic["score"],
                "script": script,
                "generated_at": datetime.now(timezone.utc).isoformat(),
                "model_used": MODEL,
                "status": "draft",
            }
            packets.append(packet)
            print(f"     ✅ Hook: \"{script.get('hook', 'N/A')[:50]}...\"")
        except Exception as e:
            print(f"     ❌ Error: {e}")

    # Write content packets
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M")
    outfile = data_dir / f"content_packets_{timestamp}.json"
    with open(outfile, "w") as f:
        json.dump({"packets": packets, "count": len(packets), "generated_at": datetime.now(timezone.utc).isoformat()}, f, indent=2)

    print(f"\n[content] Done! {len(packets)} content packets → {outfile}")
    return outfile, packets


if __name__ == "__main__":
    main()
