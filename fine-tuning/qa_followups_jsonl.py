#!/usr/bin/env python3
"""QA a JSONL file of items shaped like {"messages": [...]}.

Prints summary stats + a few example failures.
Exit code 0 if no invalid lines, else 2.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter


def is_valid(obj):
    if not isinstance(obj, dict):
        return False, "not_dict"
    msgs = obj.get("messages")
    if not isinstance(msgs, list):
        return False, "messages_not_list"
    if len(msgs) < 2:
        return False, "too_few_messages"
    # alternating roles, starting with user
    for i, m in enumerate(msgs):
        if not isinstance(m, dict):
            return False, f"msg_{i}_not_dict"
        role = m.get("role")
        content = m.get("content")
        if role not in ("user", "assistant"):
            return False, f"msg_{i}_bad_role"
        if not isinstance(content, str) or not content.strip():
            return False, f"msg_{i}_empty_content"
        if i % 2 == 0 and role != "user":
            return False, f"msg_{i}_role_not_user"
        if i % 2 == 1 and role != "assistant":
            return False, f"msg_{i}_role_not_assistant"
    return True, "ok"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--max-bad", type=int, default=10)
    args = ap.parse_args()

    total = 0
    ok = 0
    bad = 0
    msg_lens = Counter()
    reasons = Counter()
    bad_examples = []

    with open(args.path, "r", encoding="utf-8") as f:
        for ln, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            total += 1
            try:
                obj = json.loads(line)
            except Exception as e:
                bad += 1
                reasons["json_parse"] += 1
                if len(bad_examples) < args.max_bad:
                    bad_examples.append((ln, "json_parse", str(e), line[:300]))
                continue

            valid, reason = is_valid(obj)
            if valid:
                ok += 1
                msg_lens[len(obj["messages"])] += 1
            else:
                bad += 1
                reasons[reason] += 1
                if len(bad_examples) < args.max_bad:
                    bad_examples.append((ln, reason, "", line[:300]))

    print(f"file={args.path}")
    print(f"total_lines={total} ok={ok} bad={bad}")
    if msg_lens:
        print("messages_len_counts=" + ", ".join(f"{k}:{v}" for k, v in sorted(msg_lens.items())))
    if reasons:
        print("bad_reasons=" + ", ".join(f"{k}:{v}" for k, v in reasons.most_common()))
    if bad_examples:
        print("\nBAD EXAMPLES:")
        for ln, reason, err, snippet in bad_examples:
            print(f"- line {ln}: {reason} {err}")
            print(f"  {snippet}")

    raise SystemExit(0 if bad == 0 else 2)


if __name__ == "__main__":
    main()
