#!/usr/bin/env python3
"""Generate TOEFL-style scaffolding dialogues using Gemini CLI.

Why this exists:
- `generate_scaffolding_dialogues.py` is hard-wired to OpenRouter + Kimi.
- You asked to switch synthetic generation to Gemini (e.g. gemini-3-flash-preview).

This script:
- Samples TOEFL11-like error patterns (L1 + error type)
- Prompts Gemini to output a 4-line Student/Teacher dialogue (no explicit rule explanation)
- Parses into OpenAI-style `messages` and writes JSONL
- Retries on transient failures (incl. 429 capacity)

Usage:
  python3 generate_scaffolding_dialogues_gemini.py \
    --count 10000 \
    --model gemini-3-flash-preview \
    --output data/toefl_synth_followups_10000_gemini-3-flash-preview_$(date +%Y%m%d_%H%M).jsonl

Notes:
- Requires `gemini` CLI installed + authenticated.
"""

from __future__ import annotations

import argparse
import json
import random
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


ERROR_PATTERNS = {
    "Spanish": [
        {"error": "She is teacher", "correct": "She is a teacher", "type": "article_omission"},
        {"error": "I have three book", "correct": "I have three books", "type": "plural_omission"},
        {"error": "Yesterday I go to store", "correct": "Yesterday I went to the store", "type": "past_tense"},
        {"error": "He want to eat", "correct": "He wants to eat", "type": "verb_agreement"},
        {"error": "I am agree with you", "correct": "I agree with you", "type": "be_verb_overuse"},
    ],
    "Chinese": [
        {"error": "I have three book", "correct": "I have three books", "type": "plural_omission"},
        {"error": "Yesterday I go to school", "correct": "Yesterday I went to school", "type": "past_tense"},
        {"error": "She is very beautiful girl", "correct": "She is a very beautiful girl", "type": "article_omission"},
        {"error": "I very like this", "correct": "I really like this", "type": "adverb_placement"},
        {"error": "He go to work everyday", "correct": "He goes to work everyday", "type": "verb_agreement"},
    ],
    "Arabic": [
        {"error": "She is good teacher", "correct": "She is a good teacher", "type": "article_omission"},
        {"error": "I have many informations", "correct": "I have a lot of information", "type": "uncountable_plural"},
        {"error": "He is very tall man", "correct": "He is a very tall man", "type": "article_omission"},
        {"error": "I go to school yesterday", "correct": "I went to school yesterday", "type": "past_tense"},
        {"error": "They was happy", "correct": "They were happy", "type": "verb_agreement"},
    ],
}


SCAFFOLDING_TEMPLATE = """Generate a natural 3-4 turn teacher-student dialogue where:
- Student (native {l1} speaker, {level} English) makes this error: "{error}"
- Teacher uses adaptive scaffolding: asks questions, recasts naturally, or expands (NO explicit correction)
- Student responds
- Teacher encourages

The teacher should model the correct form "{correct}" naturally without saying "that's wrong" or explaining rules.

Return ONLY the dialogue in this exact format (4 lines):
Student: ...
Teacher: ...
Student: ...
Teacher: ...
"""


@dataclass
class GeminiResult:
    ok: bool
    text: str
    stderr: str
    returncode: int


def call_gemini(prompt: str, model: str, timeout_s: int) -> GeminiResult:
    # Use positional prompt (one-shot), with explicit output format.
    # NOTE: The CLI supports -o json, but the wrapper output can be verbose; text is simpler to parse.
    cmd = ["gemini", "-m", model, "-o", "text", prompt]
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout_s)
        stdout = (p.stdout or "").strip()
        stderr = (p.stderr or "").strip()
        return GeminiResult(ok=(p.returncode == 0 and len(stdout) > 0), text=stdout, stderr=stderr, returncode=p.returncode)
    except subprocess.TimeoutExpired as e:
        return GeminiResult(ok=False, text="", stderr=f"TIMEOUT after {timeout_s}s: {e}", returncode=124)


def parse_dialogue(text: str):
    msgs = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line.startswith("Student:"):
            msgs.append({"role": "user", "content": line[len("Student:"):].strip()})
        elif line.startswith("Teacher:"):
            msgs.append({"role": "assistant", "content": line[len("Teacher:"):].strip()})

    # Expect 4 messages (user/assistant/user/assistant). If not, treat as failure.
    if len(msgs) != 4:
        return None
    if msgs[0]["role"] != "user" or msgs[1]["role"] != "assistant" or msgs[2]["role"] != "user" or msgs[3]["role"] != "assistant":
        return None
    if any(m["content"] == "" for m in msgs):
        return None
    return msgs


def looks_like_capacity_or_rate_limit(stderr: str) -> bool:
    s = (stderr or "").lower()
    return (
        "no capacity" in s
        or "resource_exhausted" in s
        or "model_capacity_exhausted" in s
        or "429" in s
        or "too many requests" in s
        or "rate" in s and "limit" in s
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="data/toefl_synth_followups_gemini.jsonl")
    ap.add_argument("--count", type=int, default=1000)
    ap.add_argument("--model", default="gemini-3-flash-preview")
    ap.add_argument("--timeout", type=int, default=90, help="Per-request timeout (seconds)")
    ap.add_argument("--max-retries", type=int, default=8)
    ap.add_argument("--min-backoff", type=float, default=2.0)
    ap.add_argument("--max-backoff", type=float, default=60.0)
    ap.add_argument("--debug", action="store_true")
    args = ap.parse_args()

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    generated = 0
    attempts = 0

    # Write line-by-line for durability.
    with out_path.open("w", encoding="utf-8") as f:
        while generated < args.count:
            l1 = random.choice(list(ERROR_PATTERNS.keys()))
            pattern = random.choice(ERROR_PATTERNS[l1])
            level = random.choice(["beginner", "intermediate"])

            prompt = SCAFFOLDING_TEMPLATE.format(
                l1=l1,
                level=level,
                error=pattern["error"],
                correct=pattern["correct"],
            )

            ok = False
            last_err = ""
            last_text = ""

            for retry in range(args.max_retries + 1):
                attempts += 1
                res = call_gemini(prompt, model=args.model, timeout_s=args.timeout)
                last_err = res.stderr
                last_text = res.text

                if res.ok:
                    msgs = parse_dialogue(res.text)
                    if msgs:
                        record = {
                            "l1_background": l1,
                            "proficiency": level,
                            "error_type": pattern["type"],
                            "error_pattern": pattern["error"],
                            "correct_form": pattern["correct"],
                            "messages": msgs,
                        }
                        f.write(json.dumps(record, ensure_ascii=False) + "\n")
                        f.flush()
                        generated += 1
                        ok = True
                        print(f"[{generated}/{args.count}] {l1} ({level}) - {pattern['type']}")
                        break

                # Retry logic
                backoff = min(args.max_backoff, args.min_backoff * (2 ** retry))
                if looks_like_capacity_or_rate_limit(res.stderr):
                    # Capacity issues: exponential backoff
                    time.sleep(backoff)
                    continue

                # Other errors: short backoff + one more try
                time.sleep(min(5.0, backoff))

            if not ok:
                # Write a minimal failure line so we can account for gaps if needed
                if args.debug:
                    sys.stderr.write("\n--- FAILED EXAMPLE ---\n")
                    sys.stderr.write(f"model={args.model}\n")
                    sys.stderr.write(f"stderr={last_err[:2000]}\n")
                    sys.stderr.write(f"text={last_text[:2000]}\n")
                    sys.stderr.write("\n----------------------\n")

                # Don’t spin forever on persistent failures
                print(f"❌ Failed after retries (generated={generated}/{args.count}). Continuing…", file=sys.stderr)
                continue

    print(f"\n✅ Done. Wrote {generated} examples to {out_path}")
    print(f"Total attempts: {attempts}")


if __name__ == "__main__":
    main()
