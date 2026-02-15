#!/usr/bin/env python3
"""Prepare Stage 1 mix JSONL by downloading HF datasets directly.

Mix includes:
- UltraChat (local JSONLs already in fine-tuning/data)
- LMSYS-Chat-1M (HF)
- Magpie (HF)
- Prosocial Dialog (HF)
- TOEFL synth follow-ups (local JSONLs)

Output format: JSONL lines of {"messages": [{"role":...,"content":...}, ...]}

Notes
- Does NOT include Wikitext (per user instruction).
- Uses HF_TOKEN if set.

Example:
  python prepare_stage1_mix_hf.py \
    --out data/stage1_mix_20260214.jsonl \
    --ultrachat data/ultrachat_200k_train_sft.jsonl \
    --ultrachat data/ultrachat_200k_train_sft_cuny_es.jsonl \
    --toefl data/toefl_synth_followups_5k_2turn_gemini3flash_openrouter_20260212_1922.jsonl \
    --lmsys-samples 50000 --magpie-samples 100000 --prosocial-samples 20000 \
    --ultrachat-samples 100000 --toefl-samples 10000
"""

import argparse
import json
import os
import random
from pathlib import Path
from typing import Iterable, Dict, Any, List, Optional

from datasets import load_dataset


def iter_jsonl(path: Path):
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except Exception:
                continue


def write_jsonl(out: Path, items: Iterable[Dict[str, Any]]):
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for obj in items:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


def take_random(dataset, n: int, seed: int):
    # datasets supports shuffle+select
    if n <= 0:
        return dataset
    if n >= len(dataset):
        return dataset
    return dataset.shuffle(seed=seed).select(range(n))


def norm_messages(msgs: Any) -> Optional[List[Dict[str, str]]]:
    if not isinstance(msgs, list) or len(msgs) < 2:
        return None
    out = []
    for m in msgs:
        if not isinstance(m, dict):
            return None
        role = m.get("role")
        content = m.get("content")
        if role not in ("user", "assistant", "system"):
            return None
        if not isinstance(content, str) or not content.strip():
            return None
        out.append({"role": role, "content": content.strip()})
    # require at least one assistant
    if not any(m["role"] == "assistant" for m in out):
        return None
    return out


def lmsys_to_messages(row: Dict[str, Any]) -> Optional[List[Dict[str, str]]]:
    conv = row.get("conversation")
    if not isinstance(conv, list):
        return None
    msgs = []
    for t in conv:
        if isinstance(t, dict):
            role = t.get("role")
            content = t.get("content")
            if role in ("user", "assistant") and isinstance(content, str) and content.strip():
                msgs.append({"role": role, "content": content.strip()})
    return msgs if len(msgs) >= 2 else None


def magpie_to_messages(row: Dict[str, Any]) -> Optional[List[Dict[str, str]]]:
    conv = row.get("conversations")
    if not isinstance(conv, list):
        return None
    msgs = []
    for t in conv:
        if isinstance(t, dict):
            frm = t.get("from")
            val = t.get("value")
            if not (isinstance(val, str) and val.strip()):
                continue
            role = "user" if frm == "human" else "assistant"
            msgs.append({"role": role, "content": val.strip()})
    return msgs if len(msgs) >= 2 else None


def prosocial_to_messages(row: Dict[str, Any]) -> Optional[List[Dict[str, str]]]:
    context = row.get("context")
    response = row.get("response")
    if isinstance(context, str) and context.strip() and isinstance(response, str) and response.strip():
        return [{"role": "user", "content": context.strip()}, {"role": "assistant", "content": response.strip()}]
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=42)

    ap.add_argument("--ultrachat", action="append", default=[])
    ap.add_argument("--toefl", action="append", default=[])

    ap.add_argument("--ultrachat-samples", type=int, default=100000)
    ap.add_argument("--toefl-samples", type=int, default=10000)
    ap.add_argument("--lmsys-samples", type=int, default=50000)
    ap.add_argument("--magpie-samples", type=int, default=100000)
    ap.add_argument("--prosocial-samples", type=int, default=20000)

    args = ap.parse_args()
    random.seed(args.seed)

    out_path = Path(args.out)
    items: List[Dict[str, Any]] = []

    # Local UltraChat JSONLs
    for p in args.ultrachat:
        path = Path(p)
        if not path.exists():
            print(f"[ultrachat] missing: {path}")
            continue
        # reservoir-ish: take first N valid for now (fast, deterministic). Optionally could random sample.
        kept = 0
        for ex in iter_jsonl(path):
            msgs = norm_messages(ex.get("messages"))
            if not msgs:
                continue
            items.append({"messages": msgs})
            kept += 1
            if kept >= args.ultrachat_samples:
                break
        print(f"[ultrachat] {path.name}: kept {kept}")

    # Local TOEFL followups JSONLs
    for p in args.toefl:
        path = Path(p)
        if not path.exists():
            print(f"[toefl] missing: {path}")
            continue
        kept = 0
        for ex in iter_jsonl(path):
            msgs = norm_messages(ex.get("messages"))
            if not msgs:
                continue
            items.append({"messages": msgs})
            kept += 1
            if kept >= args.toefl_samples:
                break
        print(f"[toefl] {path.name}: kept {kept}")

    # HF datasets
    # LMSYS
    print("[hf] loading lmsys-chat-1m...")
    lmsys = load_dataset("lmsys/lmsys-chat-1m", split="train")
    lmsys = take_random(lmsys, args.lmsys_samples, args.seed)
    kept = 0
    for row in lmsys:
        msgs = lmsys_to_messages(row)
        if msgs:
            items.append({"messages": msgs})
            kept += 1
    print(f"[hf] lmsys kept {kept}")

    # Magpie
    print("[hf] loading Magpie...")
    magpie = load_dataset("Magpie-Align/magpie-llama-3.1-pro-300k-filtered", split="train")
    magpie = take_random(magpie, args.magpie_samples, args.seed + 1)
    kept = 0
    for row in magpie:
        msgs = magpie_to_messages(row)
        if msgs:
            items.append({"messages": msgs})
            kept += 1
    print(f"[hf] magpie kept {kept}")

    # Prosocial
    print("[hf] loading prosocial-dialog...")
    prosocial = load_dataset("allenai/prosocial-dialog", split="train")
    prosocial = take_random(prosocial, args.prosocial_samples, args.seed + 2)
    kept = 0
    for row in prosocial:
        msgs = prosocial_to_messages(row)
        if msgs:
            items.append({"messages": msgs})
            kept += 1
    print(f"[hf] prosocial kept {kept}")

    random.shuffle(items)
    write_jsonl(out_path, items)
    print(f"Wrote {len(items)} examples -> {out_path}")


if __name__ == "__main__":
    # Make HF downloads non-interactive
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
    main()
