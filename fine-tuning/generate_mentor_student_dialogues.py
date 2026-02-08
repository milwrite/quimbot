#!/usr/bin/env python3
"""Generate mentor-student dialogues in Education-Dialogue-Dataset format.
Outputs JSONL with fields: background_info, conversation (list of {role,text}), probability.
"""
import argparse, json, os, random, time
import requests

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
DEFAULT_MODEL = os.getenv("OPENROUTER_MODEL", "moonshotai/kimi-k2.5")

SYSTEM = (
    "You generate educational mentor-student dialogues. "
    "Return STRICT JSON only (no code fences), with keys: "
    "background_info {topic, student_preferences, teacher_preferences, student_reactions, teacher_reactions}, "
    "conversation (list of {role, text}), probability (float 0-1). "
    "Conversation is 10-15 turns, ends with [end of conversation] in the final turn."
)

TOPICS = [
    "past tense verbs", "articles (a/the)", "subject-verb agreement",
    "code-switching in bilingual settings", "academic email etiquette",
    "museum label writing", "summarizing an article", "asking clarifying questions",
]
STUDENT_PREFS = ["hands-on activities", "examples", "short explanations", "visual aids", "discussion"]
TEACHER_PREFS = ["Socratic questioning", "examples", "guided practice", "mini-lecture"]
STUDENT_REACTIONS = ["gets disengaged", "asks for clarification", "tries another method", "becomes frustrated"]
TEACHER_REACTIONS = ["adapts to student", "offers a new example", "gets briefly frustrated then adjusts"]


def call_openrouter(prompt, api_key, model=DEFAULT_MODEL, temp=0.7, max_tokens=300):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "X-Title": "quimbot-mentor-student-gen",
    }
    payload = {
        "model": model,
        "temperature": temp,
        "max_tokens": max_tokens,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": prompt},
        ],
    }
    r = requests.post(OPENROUTER_URL, headers=headers, json=payload, timeout=90)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip()


def make_prompt():
    topic = random.choice(TOPICS)
    sp = random.choice(STUDENT_PREFS)
    tp = random.choice(TEACHER_PREFS)
    sr = random.choice(STUDENT_REACTIONS)
    tr = random.choice(TEACHER_REACTIONS)
    return (
        f"Simulate an informal dialogue between a college mentor and a student. "
        f"There is a small chance the mentor is successful. "
        f"The conversation lasts 10-15 turns and ends when either side says [end of conversation]. "
        f"The mentor wants to teach the student about {topic}. "
        f"The student likes {sp}. The mentor does not know beforehand. "
        f"If the student doesn't get their preference, the student {sr}. "
        f"The teacher prefers {tp}; if the student doesn't learn that way, the teacher {tr}. "
        f"Return JSON only in the required schema."
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", required=True)
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--sleep", type=float, default=0.0)
    ap.add_argument("--max-tokens", type=int, default=300)
    args = ap.parse_args()

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise SystemExit("Missing OPENROUTER_API_KEY")

    with open(args.output, "w", encoding="utf-8") as f:
        for i in range(1, args.n + 1):
            prompt = make_prompt()
            text = call_openrouter(prompt, api_key, model=args.model, max_tokens=args.max_tokens)
            # best-effort JSON parse
            try:
                obj = json.loads(text)
            except json.JSONDecodeError:
                # fallback: wrap raw text
                obj = {"raw": text}
            f.write(json.dumps(obj) + "\n")
            if i % 50 == 0 or i == 1:
                print(f"[{i}/{args.n}] ok")
            time.sleep(args.sleep)

    print(f"Wrote {args.n} examples to {args.output}")


if __name__ == "__main__":
    main()
