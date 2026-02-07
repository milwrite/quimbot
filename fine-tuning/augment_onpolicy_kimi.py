#!/usr/bin/env python3
"""
Generate scaffolding responses (no explicit correction) from TOEFL-style error prompts
using OpenRouter (Kimi 2.5).

Outputs JSONL with {messages:[{role,user},{role,assistant}]} entries.
"""
import argparse, json, os, time
import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = os.getenv("OPENROUTER_MODEL", "moonshotai/kimi-k2")

SYSTEM = (
    "You are a supportive language-learning partner. "
    "Use scaffolding (recasts, hints, questions). "
    "Do NOT explicitly say the student is wrong or give direct corrections. "
    "Ask a follow-up question that helps the student self-correct."
)

SEED_ERRORS = [
    "Technology help us communicate with people around the world.",
    "I have three book on my desk.",
    "Yesterday I go to the store.",
    "She is teacher at my school.",
    "He don’t like coffee.",
]


def call_openrouter(prompt, api_key, model=DEFAULT_MODEL, temp=0.7):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-Title": "quimbot-onpolicy-scaffold",
    }
    payload = {
        "model": model,
        "temperature": temp,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
    }
    r = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=60)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--max", type=int, default=5)
    ap.add_argument("--sleep", type=float, default=0.5)
    args = ap.parse_args()

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("Missing OPENROUTER_API_KEY")

    examples = SEED_ERRORS[: args.max]
    with open(args.output, "w", encoding="utf-8") as f:
        for i, err in enumerate(examples, 1):
            resp = call_openrouter(err, api_key, model=args.model)
            obj = {
                "messages": [
                    {"role": "user", "content": err},
                    {"role": "assistant", "content": resp},
                ]
            }
            f.write(json.dumps(obj) + "\n")
            print(f"[{i}/{len(examples)}] ok")
            time.sleep(args.sleep)

    print(f"Wrote {len(examples)} examples to {args.output}")


if __name__ == "__main__":
    main()
