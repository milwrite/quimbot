#!/usr/bin/env python3
"""Generate expanded TOEFL seed error bank using a fast LLM."""
import json, os, sys
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
    default_headers={
        "HTTP-Referer": "https://github.com/milwrite/quimbot",
        "X-Title": "quimbot-toefl-seeds",
    },
)

PROMPT = """Generate exactly 100 unique English sentences containing common ESL/TOEFL grammatical errors.
Each sentence should contain exactly ONE error. Cover these error types:
article_omission, article_overuse, past_tense, tense_form, future_after, subject_verb,
preposition, word_order, negation, comparative, superlative, pronoun_copy, pronoun_case,
participle_confusion, uncountable, subject_omission, be_overuse, gerund_infinitive,
conjunction, l1_transfer, adverb_form, verb_pattern, modal_error, passive_error,
relative_clause, conditional_error, reported_speech, double_negative

Make every sentence unique and realistic - things a real ESL student would say.
Vary topics: school, work, family, travel, food, hobbies, weather, health, technology.

Output ONLY a JSON array: [{"s": "sentence", "type": "error_type"}, ...]
No markdown fencing. No explanation. Just the JSON array."""

all_seeds = []
for batch in range(5):
    print(f"Batch {batch+1}/5...", flush=True)
    resp = client.chat.completions.create(
        model="google/gemini-2.0-flash-001",
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=8000,
        temperature=1.0,
    )
    text = resp.choices[0].message.content.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
        text = text.rsplit("```", 1)[0]
    try:
        seeds = json.loads(text)
        all_seeds.extend(seeds)
        print(f"  Got {len(seeds)} seeds (total: {len(all_seeds)})")
    except json.JSONDecodeError as e:
        print(f"  Parse error: {e}", file=sys.stderr)

# Dedup by sentence
seen = set()
unique = []
for s in all_seeds:
    if s["s"] not in seen:
        seen.add(s["s"])
        unique.append(s)

outpath = "fine-tuning/data/expanded_seeds.json"
with open(outpath, "w") as f:
    json.dump(unique, f, indent=2)
print(f"\nTotal unique seeds: {len(unique)}")
print(f"Saved to: {outpath}")
