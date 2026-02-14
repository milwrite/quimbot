#!/usr/bin/env python3
"""Quality audit for synthetic JSONL training files.

Checks per file:
1. messages length distribution, alternating role check
2. Empty/short assistant content, "As an AI" boilerplate rate
3. Duplicate detection (hash normalized assistant output)
4. Broken records: nulls, placeholder tokens, malformed JSON

Usage:
    python audit_jsonl.py [FILES...] [--out-report toefl_audit_report.json] [--out-samples toefl_audit_samples.md]

If no files given, audits all *.jsonl in fine-tuning/ and fine-tuning/data/.
"""

import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

BOILERPLATE_PATTERNS = [
    r"as an ai",
    r"as a language model",
    r"i don't have personal",
    r"i cannot provide",
    r"i'm just an ai",
    r"as an artificial intelligence",
]
PLACEHOLDER_PATTERNS = [
    r"\{?\{[A-Z_]+\}?\}",  # {{PLACEHOLDER}} or {PLACEHOLDER}
    r"<\|.*?\|>",           # <|special_token|>
    r"\[INST\]",
    r"\[/INST\]",
]
SHORT_THRESHOLD = 10  # chars


def normalize(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def hash_text(text):
    return hashlib.md5(normalize(text).encode()).hexdigest()


def audit_file(path):
    results = {
        "file": str(path),
        "size_bytes": os.path.getsize(path),
        "total_records": 0,
        "parse_errors": 0,
        "msg_len_distribution": Counter(),
        "role_alternation_violations": 0,
        "empty_content": 0,
        "short_assistant": 0,
        "boilerplate_count": 0,
        "placeholder_count": 0,
        "null_fields": 0,
        "duplicate_assistant_hashes": Counter(),
        "flagged_samples": [],
    }

    assistant_hashes = Counter()

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError:
                    results["parse_errors"] += 1
                    results["flagged_samples"].append({
                        "line": line_num, "issue": "parse_error",
                        "snippet": line[:200]
                    })
                    continue

                results["total_records"] += 1
                messages = record.get("messages", [])
                results["msg_len_distribution"][len(messages)] += 1

                # Check alternating roles
                expected_roles = ["system", "user", "assistant"]
                prev_role = None
                for i, msg in enumerate(messages):
                    role = msg.get("role", "")
                    content = msg.get("content")

                    # Null check
                    if content is None:
                        results["null_fields"] += 1
                        results["flagged_samples"].append({
                            "line": line_num, "issue": "null_content",
                            "role": role, "msg_idx": i
                        })
                        content = ""

                    # Role alternation (user/assistant should alternate after system)
                    if prev_role and role == prev_role and role in ("user", "assistant"):
                        results["role_alternation_violations"] += 1

                    # Assistant-specific checks
                    if role == "assistant":
                        h = hash_text(content)
                        assistant_hashes[h] += 1

                        if not content.strip():
                            results["empty_content"] += 1
                            results["flagged_samples"].append({
                                "line": line_num, "issue": "empty_assistant",
                                "msg_idx": i
                            })
                        elif len(content.strip()) < SHORT_THRESHOLD:
                            results["short_assistant"] += 1

                        lower = content.lower()
                        for pat in BOILERPLATE_PATTERNS:
                            if re.search(pat, lower):
                                results["boilerplate_count"] += 1
                                if len(results["flagged_samples"]) < 50:
                                    results["flagged_samples"].append({
                                        "line": line_num, "issue": "boilerplate",
                                        "snippet": content[:150], "msg_idx": i
                                    })
                                break

                    # Placeholder check on all messages
                    for pat in PLACEHOLDER_PATTERNS:
                        if re.search(pat, content):
                            results["placeholder_count"] += 1
                            if len(results["flagged_samples"]) < 50:
                                results["flagged_samples"].append({
                                    "line": line_num, "issue": "placeholder",
                                    "snippet": content[:150], "msg_idx": i
                                })
                            break

                    prev_role = role

    except Exception as e:
        results["parse_errors"] += 1
        results["flagged_samples"].append({"issue": "file_error", "error": str(e)})

    # Duplicate summary
    dupes = {h: c for h, c in assistant_hashes.items() if c > 1}
    results["unique_assistant_responses"] = len(assistant_hashes)
    results["duplicate_groups"] = len(dupes)
    results["total_duplicate_responses"] = sum(c - 1 for c in dupes.values())
    del results["duplicate_assistant_hashes"]

    # Convert Counter to dict for JSON
    results["msg_len_distribution"] = dict(sorted(results["msg_len_distribution"].items()))

    return results


def write_report(all_results, out_path):
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"Report written to {out_path}")


def write_samples(all_results, out_path):
    with open(out_path, "w") as f:
        f.write("# JSONL Audit — Flagged Samples\n\n")
        for r in all_results:
            f.write(f"## `{r['file']}`\n\n")
            f.write(f"- Records: {r['total_records']}, Parse errors: {r['parse_errors']}\n")
            f.write(f"- Empty assistant: {r['empty_content']}, Short: {r['short_assistant']}\n")
            f.write(f"- Boilerplate: {r['boilerplate_count']}, Placeholders: {r['placeholder_count']}\n")
            f.write(f"- Role violations: {r['role_alternation_violations']}\n")
            f.write(f"- Duplicates: {r['total_duplicate_responses']} dupes across {r['duplicate_groups']} groups\n")
            f.write(f"- Null fields: {r['null_fields']}\n\n")
            if r["flagged_samples"]:
                f.write("### Flagged\n\n")
                for s in r["flagged_samples"][:10]:
                    f.write(f"- Line {s.get('line','?')}: **{s['issue']}**")
                    if "snippet" in s:
                        f.write(f" — `{s['snippet'][:80]}…`")
                    f.write("\n")
                if len(r["flagged_samples"]) > 10:
                    f.write(f"- … and {len(r['flagged_samples']) - 10} more\n")
                f.write("\n")
    print(f"Samples written to {out_path}")


def main():
    parser = argparse.ArgumentParser(description="Audit JSONL training files")
    parser.add_argument("files", nargs="*", help="JSONL files to audit")
    parser.add_argument("--out-report", default="toefl_audit_report.json")
    parser.add_argument("--out-samples", default="toefl_audit_samples.md")
    parser.add_argument("--skip-large", action="store_true",
                        help="Skip files > 50MB")
    args = parser.parse_args()

    if args.files:
        files = [Path(f) for f in args.files]
    else:
        base = Path(__file__).parent
        files = sorted(base.glob("*.jsonl")) + sorted((base / "data").glob("*.jsonl"))

    all_results = []
    for f in files:
        if not f.exists():
            print(f"SKIP (not found): {f}")
            continue
        if args.skip_large and f.stat().st_size > 50_000_000:
            print(f"SKIP (>50MB): {f} ({f.stat().st_size / 1e6:.1f}MB)")
            continue
        print(f"Auditing {f} ({f.stat().st_size / 1024:.1f}KB)...")
        result = audit_file(f)
        all_results.append(result)

    write_report(all_results, args.out_report)
    write_samples(all_results, args.out_samples)

    # Summary
    print("\n=== SUMMARY ===")
    for r in all_results:
        name = os.path.basename(r["file"])
        issues = r["parse_errors"] + r["empty_content"] + r["boilerplate_count"] + r["placeholder_count"] + r["null_fields"]
        status = "✅" if issues == 0 else f"⚠️ {issues} issues"
        print(f"  {name}: {r['total_records']} records, {r['total_duplicate_responses']} dupes — {status}")


if __name__ == "__main__":
    main()
