#!/usr/bin/env python3
"""Build Stage 1 training mix from blessed supersets + HF sources.

Ratios (target): LMSYS 40% / Magpie 25% / TOEFL 20% / Prosocial 10% / Pilot 5%
TOEFL and Pilot are fixed-size local supersets; HF sources are sampled to hit ratios.

Pilot is capped at available records (1366), so effective ratio will be ~3%.
Remaining budget redistributed proportionally across HF sources.
"""

import json
import hashlib
import os
import random
import sys
from datetime import datetime
from pathlib import Path

# Try HF datasets import
try:
    from datasets import load_dataset
except ImportError:
    print("ERROR: 'datasets' not installed. Run: pip install datasets")
    sys.exit(1)

SEED = 42
random.seed(SEED)

DATA_DIR = Path(__file__).parent / "data"
OUT_NAME = f"stage1_mix_v2_{datetime.now().strftime('%Y%m%d')}.jsonl"
OUT_PATH = DATA_DIR / OUT_NAME
MANIFEST_PATH = DATA_DIR / f"stage1_mix_v2_{datetime.now().strftime('%Y%m%d')}_manifest.json"

# Local supersets (use all rows)
TOEFL_PATH = DATA_DIR / "combined_toefl_superset2_clean_dedup_20260219.jsonl"
PILOT_PATH = DATA_DIR / "combined_pilot_superset3_clean_dedup_20260219.jsonl"

# Target ratios
RATIOS = {"lmsys": 0.40, "magpie": 0.25, "toefl": 0.20, "prosocial": 0.10, "pilot": 0.05}


def iter_jsonl(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    yield json.loads(line)
                except json.JSONDecodeError:
                    continue


def msg_hash(messages):
    return hashlib.sha256(json.dumps(messages, sort_keys=True, ensure_ascii=False).encode()).hexdigest()


def norm_messages(msgs):
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
    if not any(m["role"] == "assistant" for m in out):
        return None
    return out


def lmsys_to_messages(row):
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


def magpie_to_messages(row):
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


def prosocial_to_messages(row):
    context = row.get("context")
    response = row.get("response")
    if isinstance(context, str) and context.strip() and isinstance(response, str) and response.strip():
        return [{"role": "user", "content": context.strip()}, {"role": "assistant", "content": response.strip()}]
    return None


def load_local(path, label):
    items = []
    seen = set()
    for obj in iter_jsonl(path):
        msgs = norm_messages(obj.get("messages"))
        if not msgs:
            continue
        h = msg_hash(msgs)
        if h in seen:
            continue
        seen.add(h)
        items.append({"messages": msgs, "_source": label})
    print(f"[{label}] loaded {len(items)} unique records from {path.name}")
    return items


def load_hf_source(dataset_id, converter, n_samples, label):
    print(f"[{label}] loading {dataset_id} from HF...")
    ds = load_dataset(dataset_id, split="train")
    ds = ds.shuffle(seed=SEED).select(range(min(n_samples * 2, len(ds))))  # oversample then filter
    items = []
    seen = set()
    for row in ds:
        msgs = converter(row)
        if not msgs:
            continue
        h = msg_hash(msgs)
        if h in seen:
            continue
        seen.add(h)
        items.append({"messages": msgs, "_source": label})
        if len(items) >= n_samples:
            break
    print(f"[{label}] kept {len(items)} / target {n_samples}")
    return items


def main():
    os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")

    # Load local supersets (fixed size)
    toefl_items = load_local(TOEFL_PATH, "toefl")
    pilot_items = load_local(PILOT_PATH, "pilot")

    n_toefl = len(toefl_items)
    n_pilot = len(pilot_items)

    # Calculate HF target counts based on TOEFL being 20% anchor
    total_target = n_toefl / RATIOS["toefl"]
    n_lmsys = int(total_target * RATIOS["lmsys"])
    n_magpie = int(total_target * RATIOS["magpie"])
    n_prosocial = int(total_target * RATIOS["prosocial"])

    # Pilot capped
    pilot_target = int(total_target * RATIOS["pilot"])
    if n_pilot < pilot_target:
        print(f"[pilot] capped at {n_pilot} (target was {pilot_target})")

    print(f"\nTarget counts: LMSYS={n_lmsys}, Magpie={n_magpie}, Prosocial={n_prosocial}, TOEFL={n_toefl}, Pilot={n_pilot}")
    print(f"Expected total: ~{n_lmsys + n_magpie + n_prosocial + n_toefl + n_pilot}\n")

    # Load HF sources
    lmsys_items = load_hf_source("lmsys/lmsys-chat-1m", lmsys_to_messages, n_lmsys, "lmsys")
    magpie_items = load_hf_source("Magpie-Align/magpie-llama-3.1-pro-300k-filtered", magpie_to_messages, n_magpie, "magpie")
    prosocial_items = load_hf_source("allenai/prosocial-dialog", prosocial_to_messages, n_prosocial, "prosocial")

    # Combine and shuffle
    all_items = toefl_items + pilot_items + lmsys_items + magpie_items + prosocial_items
    random.shuffle(all_items)

    # Write output
    counts = {}
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        for item in all_items:
            source = item.pop("_source")
            counts[source] = counts.get(source, 0) + 1
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    total = sum(counts.values())
    print(f"\n=== Stage 1 Mix Built ===")
    print(f"Output: {OUT_PATH}")
    print(f"Total: {total}")
    for src, n in sorted(counts.items()):
        print(f"  {src}: {n} ({n/total*100:.1f}%)")

    # Write manifest
    manifest = {
        "name": "stage1_mix_v2",
        "date": datetime.now().isoformat(),
        "seed": SEED,
        "target_ratios": RATIOS,
        "actual_counts": counts,
        "total": total,
        "actual_ratios": {k: round(v / total, 4) for k, v in counts.items()},
        "inputs": {
            "toefl": str(TOEFL_PATH),
            "pilot": str(PILOT_PATH),
            "lmsys": "lmsys/lmsys-chat-1m",
            "magpie": "Magpie-Align/magpie-llama-3.1-pro-300k-filtered",
            "prosocial": "allenai/prosocial-dialog",
        },
        "output": str(OUT_PATH),
    }
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"Manifest: {MANIFEST_PATH}")


if __name__ == "__main__":
    main()
