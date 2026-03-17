#!/usr/bin/env python3
"""
Build seed sentences from TOEFL-Spell Annotations.csv.
Uses a fast LLM to wrap each real misspelling into a realistic ESL sentence.
"""
import csv
import json
import os
import sys
import random
from collections import Counter
from pathlib import Path
from openai import OpenAI

sys.stdout.reconfigure(line_buffering=True)

ANNOTATIONS = "fine-tuning/data/toefl_spell_annotations.csv"
OUTPUT = "fine-tuning/data/toefl_spell_seeds.json"


def load_misspellings(path):
    """Load unique misspelling -> correction pairs."""
    pairs = {}
    with open(path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            mis = row["Misspelling"].strip()
            cor = row["Correction"].strip()
            if mis and cor and mis != cor:
                pairs[mis] = cor
    return pairs


def build_seeds_batch(misspellings, client, model, output_path, batch_size=40):
    """Generate seed sentences in batches, writing incrementally to JSONL."""
    items = list(misspellings.items())

    # Resume support: skip already-processed misspellings
    done = set()
    if Path(output_path).exists():
        with open(output_path) as f:
            for line in f:
                d = json.loads(line)
                if "misspelling" in d:
                    done.add(d["misspelling"])
        print(f"Resuming: {len(done)} misspellings already done")
        items = [(m, c) for m, c in items if m not in done]

    total = len(done)
    with open(output_path, "a") as out:
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            error_list = "\n".join(f"- {mis} (correct: {cor})" for mis, cor in batch)
            prompt = f"""For each misspelling below, write a short, realistic sentence (5-15 words) that a TOEFL student might write, containing that exact misspelling. Sound natural as ESL writing.

{error_list}

Output ONLY a JSON array: [{{"s": "sentence", "type": "spelling", "misspelling": "word", "correction": "correct"}}]
No markdown. No explanation."""
            try:
                resp = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=4000,
                    temperature=0.7,
                )
                text = resp.choices[0].message.content.strip()
                if text.startswith("```"):
                    text = text.split("\n", 1)[1].rsplit("```", 1)[0]
                seeds = json.loads(text)
                for s in seeds:
                    out.write(json.dumps(s) + "\n")
                out.flush()
                total += len(seeds)
                print(f"  Batch {i // batch_size + 1}: +{len(seeds)} (total: {total})")
            except Exception as e:
                print(f"  Batch {i // batch_size + 1} failed: {e}", file=sys.stderr)


def main():
    pairs = load_misspellings(ANNOTATIONS)
    print(f"Loaded {len(pairs)} unique misspelling pairs from TOEFL-Spell")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
        default_headers={
            "HTTP-Referer": "https://github.com/milwrite/quimbot",
            "X-Title": "quimbot-toefl-spell-seeds",
        },
        timeout=120.0,
    )

    # Write as JSONL for incremental saving
    jsonl_output = OUTPUT.replace(".json", ".jsonl")
    build_seeds_batch(pairs, client, "google/gemini-2.0-flash-001", jsonl_output)

    # Load and dedup
    seen = set()
    unique = []
    with open(jsonl_output) as f:
        for line in f:
            d = json.loads(line)
            if d["s"] not in seen:
                seen.add(d["s"])
                unique.append(d)

    with open(OUTPUT, "w") as f:
        json.dump(unique, f, indent=2)
    print(f"\nTotal unique seeds: {len(unique)}")
    print(f"Saved to: {OUTPUT}")


if __name__ == "__main__":
    main()
