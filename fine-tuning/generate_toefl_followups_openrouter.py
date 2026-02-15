#!/usr/bin/env python3
"""Generate short TOEFL-ish followup dialogues via OpenRouter (Gemini 3 Flash).

Writes JSONL lines of shape:
{"messages": [{"role":"user","content":...}, {"role":"assistant","content":...}]}

Usage:
  python generate_toefl_followups_openrouter.py \
    --out data/toefl_synth_followups_10k_gemini3flash_openrouter_YYYYMMDD_HHMM.jsonl \
    --n 10000 --batch 100

Env:
  OPENROUTER_API_KEY (required)
  OPENROUTER_MODEL (optional, default google/gemini-3-flash-preview)
"""

import argparse
import json
import os
import random
import sys
import time
import urllib.request
from pathlib import Path

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def system_prompt_for(turns: str) -> str:
    """turns: number of messages as string ('2','3','4','5','6') or range '6-8'."""
    if turns == "2":
        return """You generate training data for an English-learning assistant.
Create VERY SHORT micro-dialogues: a learner says one sentence (often with small grammar mistakes), and a tutor responds with ONE short follow-up question.

Constraints:
- Output must be a JSON array of objects. Each object: {"messages":[...]} using role/content objects.
- Exactly 2 messages per example: user then assistant.
- The assistant must ask a single follow-up question (end with '?').
- Keep assistant response under ~20 tokens (roughly <= 120 characters). No explanations.
- Keep user message under ~15 tokens.
- Topics: everyday life, school, work, hobbies, travel, opinions; light TOEFL speaking vibe.
- No policy / refusals / meta talk.
- No markdown, no extra keys.
"""

    if turns == "3":
        return """You generate training data for an English-learning assistant.
Create SHORT 3-message dialogues: user → assistant → user.
The tutor (assistant) asks ONE brief follow-up question that elicits more detail.

Constraints:
- Output must be a JSON array of objects. Each object: {"messages":[...]}.
- Exactly 3 messages per example.
- Assistant turn: ends with a '?' and stays under ~25 tokens (<=160 chars). No long explanations.
- User turns: under ~18 tokens.
- Keep everything concrete and everyday; TOEFL speaking practice vibe.
- No policy / refusals / meta talk.
- No markdown, no extra keys.
"""

    if turns == "4":
        return """You generate training data for an English-learning assistant.
Create SHORT 4-message dialogues: user → assistant → user → assistant.
The tutor (assistant) asks brief follow-up questions that elicit more detail and gently corrects ONLY if needed (max 1 short correction).

Constraints:
- Output must be a JSON array of objects. Each object: {"messages":[...]}.
- Exactly 4 messages per example.
- Assistant turns: each ends with a '?' and stays under ~25 tokens (<=160 chars). No long explanations.
- User turns: under ~18 tokens.
- Keep everything concrete and everyday; TOEFL speaking practice vibe.
- No policy / refusals / meta talk.
- No markdown, no extra keys.
"""

    if turns == "5":
        return """You generate training data for an English-learning assistant.
Create SHORT 5-message dialogues: user → assistant → user → assistant → user.
The tutor asks brief follow-up questions that keep the learner talking; include at most 1 short correction total.

Constraints:
- Output must be a JSON array of objects. Each object: {"messages":[...]}.
- Exactly 5 messages per example.
- Assistant turns: each ends with a '?' and stays under ~25 tokens (<=160 chars).
- User turns: under ~20 tokens.
- Concrete, everyday topics; TOEFL speaking practice vibe.
- No policy / refusals / meta talk.
- No markdown, no extra keys.
"""

    if turns == "6":
        return """You generate training data for an English-learning assistant.
Create SHORT 6-message dialogues: user → assistant → user → assistant → user → assistant.
The tutor asks brief follow-up questions that keep the learner talking; include at most 1 short correction total.

Constraints:
- Output must be a JSON array of objects. Each object: {"messages":[...]}.
- Exactly 6 messages per example.
- Assistant turns: each ends with a '?' and stays under ~25 tokens (<=160 chars).
- User turns: under ~20 tokens.
- Concrete, everyday topics; TOEFL speaking practice vibe.
- No policy / refusals / meta talk.
- No markdown, no extra keys.
"""

    if turns == "6-8":
        return """You generate training data for an English-learning assistant.
Create dialogues of 6 to 8 turns (messages). Alternate user and assistant, starting with user and ending with assistant.
The tutor asks short follow-up questions, keeps the learner talking, and may include 1 concise correction total.

Constraints:
- Output must be a JSON array of objects. Each object: {"messages":[...]}.
- Each example must have 6–8 messages, alternating roles.
- Assistant messages should be short (<=25 tokens / <=160 chars), usually a single question. Avoid long explanations.
- User messages should be short (<=20 tokens).
- Topics: everyday life, school, work, hobbies, travel, opinions.
- No policy / refusals / meta talk.
- No markdown, no extra keys.
"""

    raise ValueError(f"unknown turns spec: {turns}")


USER_TEMPLATE = """Generate {k} examples. Make them diverse. Return ONLY the JSON array."""


def openrouter_chat(api_key: str, model: str, messages, temperature: float = 0.9, max_tokens: int = 2000):
    body = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "response_format": {"type": "json"},
    }

    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        OPENROUTER_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            # Optional but good practice for OpenRouter routing/analytics
            "HTTP-Referer": "https://github.com/milwrite/quimbot",
            "X-Title": "quimbot-toefl-synth",
        },
        method="POST",
    )

    with urllib.request.urlopen(req, timeout=120) as resp:
        raw = resp.read().decode("utf-8")
    j = json.loads(raw)
    text = j["choices"][0]["message"]["content"]
    return text


def coerce_json_array(text: str):
    text = text.strip()
    # common failure: fenced code blocks
    if text.startswith("```"):
        text = text.strip("`")
        # attempt to drop leading language
        if "\n" in text:
            text = text.split("\n", 1)[1]
    # find first '[' and last ']'
    if "[" in text and "]" in text:
        text = text[text.find("[") : text.rfind("]") + 1]
    return json.loads(text)


def validate_item(item, turns: str):
    if not isinstance(item, dict):
        return False
    msgs = item.get("messages")
    if not isinstance(msgs, list):
        return False

    if turns in {"2", "3", "4", "5", "6"}:
        if len(msgs) != int(turns):
            return False
    elif turns == "6-8":
        if not (6 <= len(msgs) <= 8):
            return False
    else:
        return False

    # alternating roles, starting with user
    for i, m in enumerate(msgs):
        if not isinstance(m, dict):
            return False
        role = m.get("role")
        content = m.get("content")
        if role not in ("user", "assistant"):
            return False
        if not isinstance(content, str) or not content.strip():
            return False
        if i % 2 == 0 and role != "user":
            return False
        if i % 2 == 1 and role != "assistant":
            return False

        # length caps
        if role == "assistant" and len(content) > 200:
            return False
        if role == "user" and len(content) > 200:
            return False

    # assistant messages should be questions.
    # For even-length dialogues (2/4/6) require all assistant turns end with '?'.
    # For odd-length dialogues (3/5) require the single/each assistant turn ends with '?' (still fine).
    # For 6-8 require the last assistant ends with '?'.
    if turns in ("2", "3", "4", "5", "6"):
        if not all(m["content"].strip().endswith("?") for m in msgs if m["role"] == "assistant"):
            return False
    else:
        if not msgs[-1]["content"].strip().endswith("?"):
            return False

    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--n", type=int, default=10_000)
    ap.add_argument("--batch", type=int, default=100)
    ap.add_argument("--turns", choices=["2", "3", "4", "5", "6", "6-8"], default="2")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--model", default=os.getenv("OPENROUTER_MODEL", "google/gemini-3-flash-preview"))
    ap.add_argument("--sleep", type=float, default=0.5, help="sleep between requests")
    args = ap.parse_args()

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("Missing OPENROUTER_API_KEY")

    random.seed(args.seed)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # resume support: count existing lines
    done = 0
    if out_path.exists():
        with out_path.open("r", encoding="utf-8") as f:
            for _ in f:
                done += 1
        print(f"Resuming: {done} existing lines in {out_path}")

    target = args.n
    k = args.batch

    with out_path.open("a", encoding="utf-8") as out:
        while done < target:
            want = min(k, target - done)
            messages = [
                {"role": "system", "content": system_prompt_for(args.turns)},
                {"role": "user", "content": USER_TEMPLATE.format(k=want)},
            ]
            try:
                text = openrouter_chat(api_key, args.model, messages)
                arr = coerce_json_array(text)
                if not isinstance(arr, list):
                    raise ValueError("not a list")

                kept = 0
                for item in arr:
                    if validate_item(item, args.turns):
                        out.write(json.dumps(item, ensure_ascii=False) + "\n")
                        kept += 1
                        done += 1
                        if done >= target:
                            break

                out.flush()
                print(f"batch want={want} got={len(arr)} kept={kept} total={done}/{target}")

                if kept == 0:
                    # backoff if model is misbehaving
                    time.sleep(2.0)
                else:
                    time.sleep(args.sleep)

            except Exception as e:
                print(f"ERROR: {type(e).__name__}: {e}")
                time.sleep(3.0)


if __name__ == "__main__":
    main()
