#!/usr/bin/env python3
"""
Generate 10k TOEFL-style scaffolding dialogues using ollama gemma3:27b.
Rotates system prompt every 2500 entries across 4 adaptive scaffolding measures.

Usage:
  python3 generate_toefl_ollama_10k.py [--output FILE] [--count N] [--resume]
"""

import argparse
import json
import os
import random
import sys
import time
from pathlib import Path
from openai import OpenAI

# Unbuffered output
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

# ── Seed error bank (TOEFL non-native patterns) ──────────────────────────

ERRORS = [
    # Article errors
    {"s": "She is teacher at my school.", "type": "article_omission"},
    {"s": "I want to be engineer.", "type": "article_omission"},
    {"s": "He is honest person.", "type": "article_omission"},
    {"s": "I go to the home after class.", "type": "article_overuse"},
    {"s": "The life is beautiful.", "type": "article_overuse"},
    {"s": "She has the long hair.", "type": "article_overuse"},
    # Tense errors
    {"s": "Yesterday I go to the store.", "type": "past_tense"},
    {"s": "Last week she tell me about it.", "type": "past_tense"},
    {"s": "I am lived here for three years.", "type": "tense_form"},
    {"s": "After I will finish school, I want to travel.", "type": "future_after"},
    {"s": "When I will arrive, I call you.", "type": "future_after"},
    {"s": "I have been went there before.", "type": "tense_form"},
    # Agreement errors
    {"s": "He want to eat lunch now.", "type": "subject_verb"},
    {"s": "She don't like coffee.", "type": "subject_verb"},
    {"s": "The students was happy.", "type": "subject_verb"},
    {"s": "Everyone have their own opinion.", "type": "subject_verb"},
    # Preposition errors
    {"s": "I am interested for science.", "type": "preposition"},
    {"s": "She is good in math.", "type": "preposition"},
    {"s": "I depend of my parents.", "type": "preposition"},
    {"s": "We discussed about the problem.", "type": "preposition"},
    {"s": "I arrived to the airport early.", "type": "preposition"},
    # Word order
    {"s": "I very like this movie.", "type": "word_order"},
    {"s": "Always I study in the morning.", "type": "word_order"},
    {"s": "She speaks very well English.", "type": "word_order"},
    {"s": "I studied for five years English.", "type": "word_order"},
    # Negation
    {"s": "I no understand this.", "type": "negation"},
    {"s": "She not like vegetables.", "type": "negation"},
    {"s": "I don't can swim.", "type": "negation"},
    # Comparative/superlative
    {"s": "This is more better than that.", "type": "comparative"},
    {"s": "She is more tall than me.", "type": "comparative"},
    {"s": "He is the most smartest student.", "type": "superlative"},
    # Pronoun/reference
    {"s": "My friend he is very tall.", "type": "pronoun_copy"},
    {"s": "Me and my friend went there.", "type": "pronoun_case"},
    {"s": "I am boring in this class.", "type": "participle_confusion"},
    {"s": "The movie was very interested.", "type": "participle_confusion"},
    # Uncountable nouns
    {"s": "I have many informations.", "type": "uncountable"},
    {"s": "She gave me an advice.", "type": "uncountable"},
    {"s": "I need some furnitures.", "type": "uncountable"},
    {"s": "Can you give me some waters?", "type": "uncountable"},
    # Subject omission
    {"s": "Is very hot today.", "type": "subject_omission"},
    {"s": "Is important to study.", "type": "subject_omission"},
    # Be-verb overuse
    {"s": "I am agree with you.", "type": "be_overuse"},
    {"s": "I am have a car.", "type": "be_overuse"},
    {"s": "She is enjoy the class.", "type": "be_overuse"},
    # Gerund/infinitive
    {"s": "I enjoy to play soccer.", "type": "gerund_infinitive"},
    {"s": "I want eating now.", "type": "gerund_infinitive"},
    {"s": "I can swimming.", "type": "gerund_infinitive"},
    # Conjunction
    {"s": "Although it rained, but we went.", "type": "conjunction"},
    {"s": "Because I was tired, so I slept.", "type": "conjunction"},
    # Misc L1 transfer
    {"s": "I have 20 years.", "type": "l1_transfer"},
    {"s": "She cooks very good.", "type": "adverb_form"},
    {"s": "I am agree.", "type": "be_overuse"},
    {"s": "He explained me the problem.", "type": "verb_pattern"},
    {"s": "I suggested her to come.", "type": "verb_pattern"},
]

# ── 4 System prompts: rotate every 2500 entries ──────────────────────────

SYSTEM_PROMPTS = [
    # Phase 1 (0-2499): Recast-based scaffolding
    """You are a conversational English tutor. When a learner makes a grammatical error, respond naturally by recasting their sentence correctly within your reply. Do NOT point out the error explicitly. Do NOT say "you should say" or "the correct form is." Instead, weave the correct form into a natural follow-up question or comment that continues the conversation. Keep responses to 1-3 sentences. Sound like a friendly conversation partner, not a teacher correcting homework.""",

    # Phase 2 (2500-4999): Elicitation & clarification requests
    """You are an English conversation partner who helps learners self-correct. When a learner makes a grammatical error, ask a clarification question that naturally prompts them to rephrase. Use questions like "Do you mean...?" or "So you're saying...?" or "Could you say that another way?" The goal is for the learner to notice and fix the error themselves. Never correct directly. Never label the error. Keep it conversational and supportive. 1-3 sentences max.""",

    # Phase 3 (5000-7499): Expansion & modeling
    """You are an English conversation partner. When a learner makes a grammatical error, respond by expanding on their idea using the correct grammatical form. Build on what they said with additional detail, showing the correct structure through natural modeling. For example, if they say "Yesterday I go to store," you might say "Oh, you went to the store yesterday? What did you pick up?" The learner hears the correct form in context without being corrected. 1-3 sentences. Warm, curious tone.""",

    # Phase 4 (7500-9999): Metalinguistic hints
    """You are a friendly English tutor who gives gentle metalinguistic hints. When a learner makes a grammatical error, give a brief, encouraging hint that draws attention to the relevant grammar area without stating the correction outright. For example: "Almost! Think about the past tense here." or "Good try — check the verb form." Then ask a follow-up question to keep the conversation going. Never rewrite their sentence for them. Keep responses to 1-3 sentences. Encouraging, patient tone.""",
]

PHASE_NAMES = [
    "recast",
    "elicitation",
    "expansion",
    "metalinguistic_hint",
]

def get_phase(index: int, phase_size: int = 2500):
    phase = min(index // phase_size, len(SYSTEM_PROMPTS) - 1)
    return phase, SYSTEM_PROMPTS[phase], PHASE_NAMES[phase]


def generate_one(error: dict, system_prompt: str, phase_name: str, client, index: int) -> dict | None:
    """Generate a single dialogue turn from a seed error."""
    user_msg = error["s"]

    for attempt in range(3):
        try:
            resp = client.chat.completions.create(
                model="gpt-oss:20b",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_msg},
                ],
                max_tokens=200,
                temperature=0.8,
            )
            assistant_msg = resp.choices[0].message.content.strip()

            # Basic quality filter
            if len(assistant_msg) < 5:
                continue
            bad_phrases = ["you should say", "the correct form", "grammatically",
                           "the error", "your mistake", "incorrect"]
            if any(bp in assistant_msg.lower() for bp in bad_phrases):
                continue

            return {
                "messages": [
                    {"role": "user", "content": user_msg},
                    {"role": "assistant", "content": assistant_msg},
                ],
                "error_type": error["type"],
                "scaffolding_phase": phase_name,
                "index": index,
            }

        except Exception as e:
            wait = 2 ** attempt
            print(f"  ⚠️ attempt {attempt+1} failed: {e}, retrying in {wait}s")
            time.sleep(wait)

    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="fine-tuning/data/toefl_ollama_10k.jsonl")
    parser.add_argument("--count", type=int, default=10000)
    parser.add_argument("--phase-size", type=int, default=2500)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Resume support
    start_index = 0
    if args.resume and output_path.exists():
        with output_path.open() as f:
            start_index = sum(1 for _ in f)
        print(f"📂 Resuming from index {start_index}")

    print(f"🎯 Target: {args.count} dialogues")
    print(f"📋 Error bank: {len(ERRORS)} seed patterns")
    print(f"🔄 Phase rotation every {args.phase_size} entries")
    print(f"   Phase 1 (0-{args.phase_size-1}): Recast")
    print(f"   Phase 2 ({args.phase_size}-{args.phase_size*2-1}): Elicitation")
    print(f"   Phase 3 ({args.phase_size*2}-{args.phase_size*3-1}): Expansion")
    print(f"   Phase 4 ({args.phase_size*3}-{args.count-1}): Metalinguistic Hints")
    print()

    generated = 0
    failed = 0
    mode = "a" if args.resume else "w"

    with output_path.open(mode) as f:
        for i in range(start_index, args.count):
            error = random.choice(ERRORS)
            phase_idx, sys_prompt, phase_name = get_phase(i, args.phase_size)

            result = generate_one(error, sys_prompt, phase_name, client, i)

            if result:
                f.write(json.dumps(result) + "\n")
                if generated % 10 == 0:
                    f.flush()
                generated += 1
                if generated % 100 == 0:
                    print(f"[{generated}/{args.count - start_index}] phase={phase_name} type={error['type']}")
            else:
                failed += 1

    print(f"\n{'='*60}")
    print(f"✅ Generated: {generated}")
    print(f"❌ Failed: {failed}")
    print(f"📁 Output: {output_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
