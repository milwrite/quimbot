#!/usr/bin/env python3
"""
Generate TOEFL-style scaffolding dialogues from expanded seed bank.
Uses OpenRouter with a fast model for high throughput.
"""
import argparse
import json
import os
import random
import sys
import time
from pathlib import Path
from openai import OpenAI

sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

SYSTEM_PROMPTS = [
    """You are a conversational English tutor. When a learner makes a grammatical error, respond naturally by recasting their sentence correctly within your reply. Do NOT point out the error explicitly. Do NOT say "you should say" or "the correct form is." Instead, weave the correct form into a natural follow-up question or comment that continues the conversation. Keep responses to 1-3 sentences. Sound like a friendly conversation partner, not a teacher correcting homework.""",
    """You are an English conversation partner who helps learners self-correct. When a learner makes a grammatical error, ask a clarification question that naturally prompts them to rephrase. Use questions like "Do you mean...?" or "So you're saying...?" or "Could you say that another way?" The goal is for the learner to notice and fix the error themselves. Never correct directly. Never label the error. Keep it conversational and supportive. 1-3 sentences max.""",
    """You are an English conversation partner. When a learner makes a grammatical error, respond by expanding on their idea using the correct grammatical form. Build on what they said with additional detail, showing the correct structure through natural modeling. The learner hears the correct form in context without being corrected. 1-3 sentences. Warm, curious tone.""",
    """You are a friendly English tutor who gives gentle metalinguistic hints. When a learner makes a grammatical error, give a brief, encouraging hint that draws attention to the relevant grammar area without stating the correction outright. For example: "Almost! Think about the past tense here." Then ask a follow-up question to keep the conversation going. Never rewrite their sentence for them. Keep responses to 1-3 sentences. Encouraging, patient tone.""",
]

PHASE_NAMES = ["recast", "elicitation", "expansion", "metalinguistic_hint"]

BAD_PHRASES = [
    "you should say", "the correct form", "grammatically",
    "the error", "your mistake", "incorrect", "should be",
    "correction:", "error:", "correct version",
]


def generate_one(error, system_prompt, phase_name, client, model, index, max_attempts=3):
    user_msg = error["s"]
    for attempt in range(max_attempts):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_msg},
                ],
                max_tokens=200,
                temperature=0.8,
            )
            assistant_msg = resp.choices[0].message.content.strip()
            if len(assistant_msg) < 5:
                continue
            if any(bp in assistant_msg.lower() for bp in BAD_PHRASES):
                continue
            return {
                "messages": [
                    {"role": "user", "content": user_msg},
                    {"role": "assistant", "content": assistant_msg},
                ],
            }
        except Exception as e:
            wait = 2 ** attempt
            print(f"  attempt {attempt+1} failed: {e}, retry in {wait}s", file=sys.stderr)
            time.sleep(wait)
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", default="fine-tuning/data/expanded_seeds.json")
    parser.add_argument("--output", default="fine-tuning/data/toefl_expanded_35k.jsonl")
    parser.add_argument("--count", type=int, default=35000)
    parser.add_argument("--model", default="google/gemini-2.0-flash-001")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--batch-size", type=int, default=50, help="Print progress every N")
    args = parser.parse_args()

    with open(args.seeds) as f:
        errors = json.load(f)
    print(f"Loaded {len(errors)} seed errors")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
        default_headers={
            "HTTP-Referer": "https://github.com/milwrite/quimbot",
            "X-Title": "quimbot-toefl-expanded",
        },
        timeout=90.0,
    )

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    start_index = 0
    if args.resume and output_path.exists():
        with output_path.open() as f:
            start_index = sum(1 for _ in f)
        print(f"Resuming from index {start_index}")

    print(f"Target: {args.count} | Model: {args.model} | Seeds: {len(errors)}")

    generated = 0
    failed = 0
    mode = "a" if args.resume else "w"

    with output_path.open(mode) as f:
        for i in range(start_index, args.count):
            error = random.choice(errors)
            phase_idx = (i // (args.count // 4)) % 4
            sys_prompt = SYSTEM_PROMPTS[phase_idx]
            phase_name = PHASE_NAMES[phase_idx]

            result = generate_one(error, sys_prompt, phase_name, client, args.model, i)
            if result:
                f.write(json.dumps(result) + "\n")
                generated += 1
                if generated % args.batch_size == 0:
                    f.flush()
                    print(f"[{generated}/{args.count - start_index}] phase={phase_name}")
            else:
                failed += 1

    print(f"\nGenerated: {generated} | Failed: {failed}")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()
