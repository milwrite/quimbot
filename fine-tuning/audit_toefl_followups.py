#!/usr/bin/env python3
"""Audit + (optionally) merge TOEFL synth followups JSONLs.

Usage:
  python3 fine-tuning/audit_toefl_followups.py --glob 'fine-tuning/data/toefl_synth_followups*.jsonl' --outdir fine-tuning/data/_audit
  python3 fine-tuning/audit_toefl_followups.py --glob 'fine-tuning/data/toefl_synth_followups*.jsonl' --outdir fine-tuning/data/_audit --merge-out fine-tuning/data/toefl_synth_followups_merged_20260214.jsonl

What it checks per file:
  - JSON parse validity, line counts
  - schema: expects {"messages": [{"role","content"}, ...]}
  - content empties
  - role alternation (user/assistant) + starts-with-user heuristic
  - suspicious boilerplate markers ("as an ai", "I can't", "cannot")
  - length stats (chars/tokens-ish)
  - duplicates (hash of normalized assistant messages)

It also writes a small samples markdown of flagged records.
"""

import argparse, glob, json, os, re, hashlib
from collections import Counter, defaultdict

ROLE_OK = {"user", "assistant", "system"}

BOILERPLATE_PATTERNS = [
    re.compile(r"\bas an ai\b", re.I),
    re.compile(r"\bi (?:can't|cannot)\b", re.I),
    re.compile(r"\bi don't have the ability\b", re.I),
    re.compile(r"\bi (?:am not able to|won't be able to)\b", re.I),
]
PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTODO\b"),
    re.compile(r"\bTBD\b"),
    re.compile(r"\{\{.*?\}\}"),
    re.compile(r"\[INSERT .*?\]", re.I),
]


def norm_text(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s


def hash_text(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()


def iter_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip("\n")
            if not line.strip():
                continue
            yield i, line


def analyze_record(obj):
    """Return (ok, info, flags)."""
    flags = []
    info = {
        "n_messages": None,
        "roles": [],
        "empty_contents": 0,
        "char_counts": [],
        "assistant_hashes": [],
        "boilerplate_hits": 0,
        "placeholder_hits": 0,
        "starts_with_user": None,
        "alternation_ok": None,
    }

    if not isinstance(obj, dict):
        flags.append("not_dict")
        return False, info, flags

    msgs = obj.get("messages")
    if not isinstance(msgs, list):
        flags.append("missing_messages_list")
        return False, info, flags

    info["n_messages"] = len(msgs)
    if len(msgs) == 0:
        flags.append("empty_messages")
        return False, info, flags

    roles = []
    for m in msgs:
        if not isinstance(m, dict):
            flags.append("bad_message_item")
            continue
        role = m.get("role")
        content = m.get("content")
        if role not in ROLE_OK:
            flags.append("bad_role")
        roles.append(role)
        if content is None or (isinstance(content, str) and content.strip() == ""):
            info["empty_contents"] += 1
            flags.append("empty_content")
            content = "" if content is None else content
        if isinstance(content, str):
            info["char_counts"].append(len(content))
            txtn = norm_text(content)
            if role == "assistant" and txtn:
                info["assistant_hashes"].append(hash_text(txtn))
            for pat in BOILERPLATE_PATTERNS:
                if pat.search(txtn):
                    info["boilerplate_hits"] += 1
                    flags.append("boilerplate")
                    break
            for pat in PLACEHOLDER_PATTERNS:
                if pat.search(content):
                    info["placeholder_hits"] += 1
                    flags.append("placeholder")
                    break

    info["roles"] = roles
    info["starts_with_user"] = (roles[0] == "user") if roles else None

    # Alternation heuristic: ignore system messages, expect user/assistant alternating
    seq = [r for r in roles if r in {"user", "assistant"}]
    alt_ok = True
    for a, b in zip(seq, seq[1:]):
        if a == b:
            alt_ok = False
            break
    info["alternation_ok"] = alt_ok
    if not alt_ok:
        flags.append("role_not_alternating")

    # suspicious: very short assistant response
    if any(r == "assistant" for r in roles):
        # compute min assistant char length
        # (we don't keep per-role lengths above; re-scan)
        min_assist = None
        for m in msgs:
            if isinstance(m, dict) and m.get("role") == "assistant":
                c = m.get("content")
                if isinstance(c, str):
                    L = len(c.strip())
                    min_assist = L if min_assist is None else min(min_assist, L)
        if min_assist is not None and min_assist < 40:
            flags.append("assistant_too_short")

    ok = True
    # hard failures
    if "missing_messages_list" in flags or "empty_messages" in flags or "not_dict" in flags:
        ok = False

    return ok, info, sorted(set(flags))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--glob", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--merge-out", default=None)
    ap.add_argument("--max-samples", type=int, default=60)
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    paths = sorted([p for p in glob.glob(args.glob) if not p.endswith('.log')])

    report = {
        "files": [],
        "totals": {
            "files": 0,
            "zero_bytes": 0,
            "lines": 0,
            "bad_json_lines": 0,
            "bad_schema_records": 0,
            "records": 0,
            "duplicate_assistant_hashes": 0,
        },
    }

    global_assistant_hash_seen = set()
    global_duplicate_hashes = set()

    samples = []

    merge_f = open(args.merge_out, "w", encoding="utf-8") if args.merge_out else None

    try:
        for p in paths:
            st = os.stat(p)
            file_entry = {
                "path": p,
                "size_bytes": st.st_size,
                "records": 0,
                "bad_json_lines": 0,
                "bad_schema_records": 0,
                "flags": Counter(),
                "role_counts": Counter(),
                "n_messages_hist": Counter(),
                "empty_content_records": 0,
                "boilerplate_records": 0,
                "placeholder_records": 0,
                "starts_with_user_false": 0,
                "alternation_false": 0,
                "assistant_short_records": 0,
                "duplicate_assistant_hashes_global": 0,
            }

            report["totals"]["files"] += 1
            if st.st_size == 0:
                report["totals"]["zero_bytes"] += 1
                report["files"].append({**file_entry, "zero_bytes": True})
                continue

            for line_no, line in iter_jsonl(p):
                report["totals"]["lines"] += 1
                try:
                    obj = json.loads(line)
                except Exception:
                    file_entry["bad_json_lines"] += 1
                    report["totals"]["bad_json_lines"] += 1
                    if len(samples) < args.max_samples:
                        samples.append((p, line_no, "bad_json", line[:400]))
                    continue

                ok, info, flags = analyze_record(obj)
                file_entry["records"] += 1
                report["totals"]["records"] += 1
                file_entry["n_messages_hist"][str(info.get("n_messages"))] += 1

                for r in info.get("roles") or []:
                    file_entry["role_counts"][r] += 1

                if not ok:
                    file_entry["bad_schema_records"] += 1
                    report["totals"]["bad_schema_records"] += 1

                for fl in flags:
                    file_entry["flags"][fl] += 1

                if "empty_content" in flags:
                    file_entry["empty_content_records"] += 1
                if "boilerplate" in flags:
                    file_entry["boilerplate_records"] += 1
                if "placeholder" in flags:
                    file_entry["placeholder_records"] += 1
                if info.get("starts_with_user") is False:
                    file_entry["starts_with_user_false"] += 1
                if info.get("alternation_ok") is False:
                    file_entry["alternation_false"] += 1
                if "assistant_too_short" in flags:
                    file_entry["assistant_short_records"] += 1

                # duplicates: assistant message hashes (global)
                dup_hit = False
                for h in info.get("assistant_hashes") or []:
                    if h in global_assistant_hash_seen:
                        dup_hit = True
                        global_duplicate_hashes.add(h)
                    else:
                        global_assistant_hash_seen.add(h)
                if dup_hit:
                    file_entry["duplicate_assistant_hashes_global"] += 1

                # collect samples of flagged records for quick review
                if flags and len(samples) < args.max_samples:
                    # store compact sample: roles + first 200 chars of each message
                    msgs = obj.get("messages") if isinstance(obj, dict) else None
                    preview = []
                    if isinstance(msgs, list):
                        for m in msgs[:6]:
                            if isinstance(m, dict):
                                role = m.get("role")
                                content = m.get("content")
                                if isinstance(content, str):
                                    content = content.strip().replace("\n", " ")
                                    content = content[:220]
                                preview.append({"role": role, "content": content})
                    samples.append((p, line_no, ",".join(flags), preview))

                # merge writing
                if merge_f and ok and (st.st_size > 0):
                    # annotate source
                    if isinstance(obj, dict):
                        obj = dict(obj)
                        obj["source_file"] = os.path.basename(p)
                    merge_f.write(json.dumps(obj, ensure_ascii=False) + "\n")

            # convert Counters to dicts for JSON
            file_entry["flags"] = dict(file_entry["flags"])
            file_entry["role_counts"] = dict(file_entry["role_counts"])
            file_entry["n_messages_hist"] = dict(file_entry["n_messages_hist"])
            report["files"].append(file_entry)

        report["totals"]["duplicate_assistant_hashes"] = len(global_duplicate_hashes)

        out_json = os.path.join(args.outdir, "toefl_audit_report.json")
        with open(out_json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)

        out_md = os.path.join(args.outdir, "toefl_audit_samples.md")
        with open(out_md, "w", encoding="utf-8") as f:
            f.write("# TOEFL synth followups — audit samples (flagged)\n\n")
            for p, line_no, flags, preview in samples:
                f.write(f"## {os.path.basename(p)} : line {line_no} ({flags})\n\n")
                if preview == "bad_json":
                    f.write("(bad json)\n\n")
                elif isinstance(preview, str):
                    f.write("```\n" + preview + "\n```\n\n")
                else:
                    f.write("```json\n" + json.dumps(preview, ensure_ascii=False, indent=2) + "\n```\n\n")

        # console summary
        print("Wrote:")
        print(" -", out_json)
        print(" -", out_md)
        if args.merge_out:
            print(" -", args.merge_out)
        print("Totals:", json.dumps(report["totals"], indent=2))

    finally:
        if merge_f:
            merge_f.close()


if __name__ == "__main__":
    main()
