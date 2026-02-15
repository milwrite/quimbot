#!/usr/bin/env python3
"""Consolidate multiple followups JSONL files into one canonical JSONL.

- Reads input JSONL files (glob patterns supported)
- Validates message structure (alternating roles, non-empty content)
- Drops invalid lines
- Optionally enforces message counts (e.g. 2,4,6-8)
- Writes a single output JSONL

Designed for quimbot TOEFL-ish followups datasets.
"""

from __future__ import annotations

import argparse
import glob
import json
from pathlib import Path


def valid_messages(msgs, enforce=None):
    if not isinstance(msgs, list) or len(msgs) < 2:
        return False
    if enforce is not None:
        if isinstance(enforce, set):
            if len(msgs) not in enforce:
                return False
        elif isinstance(enforce, tuple):
            lo, hi = enforce
            if not (lo <= len(msgs) <= hi):
                return False
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
    return True


def parse_enforce(spec: str | None):
    if not spec:
        return None
    spec = spec.strip()
    if spec in ("6-8", "6..8"):
        return (6, 8)
    if "," in spec:
        return {int(x.strip()) for x in spec.split(",") if x.strip()}
    return {int(spec)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inputs", action="append", required=True, help="Input file or glob. Repeatable.")
    ap.add_argument("--out", required=True)
    ap.add_argument("--enforce", default=None, help="Enforce message counts: e.g. '2' or '2,4' or '6-8'")
    args = ap.parse_args()

    enforce = parse_enforce(args.enforce)

    files = []
    for pat in args.inputs:
        expanded = sorted(glob.glob(pat))
        if expanded:
            files.extend(expanded)
        else:
            files.append(pat)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    total = 0
    kept = 0
    dropped = 0

    with out_path.open("w", encoding="utf-8") as out:
        for fp in files:
            p = Path(fp)
            if not p.exists():
                continue
            with p.open("r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    total += 1
                    try:
                        obj = json.loads(line)
                    except Exception:
                        dropped += 1
                        continue

                    msgs = obj.get("messages")
                    if not valid_messages(msgs, enforce=enforce):
                        dropped += 1
                        continue

                    out.write(json.dumps({"messages": msgs}, ensure_ascii=False) + "\n")
                    kept += 1

    print(f"inputs={len(files)} total={total} kept={kept} dropped={dropped} out={out_path}")


if __name__ == "__main__":
    main()
