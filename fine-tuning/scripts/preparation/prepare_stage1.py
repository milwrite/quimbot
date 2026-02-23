#!/usr/bin/env python3
"""
Prepare Stage 1 training data from downloaded Arrow datasets.
Combines LMSYS-Chat-1M, Magpie, and Prosocial Dialog into ChatML format.
"""

import json
import random
from pathlib import Path
import pyarrow as pa


def load_arrow_dataset(cache_dir: Path):
    """Load dataset from HuggingFace cache Arrow files."""
    arrow_files = sorted(cache_dir.glob("*.arrow"))
    if not arrow_files:
        return None
    
    tables = []
    for f in arrow_files:
        with pa.memory_map(str(f), 'r') as source:
            reader = pa.ipc.open_stream(source)
            table = reader.read_all()
            tables.append(table)
    
    return pa.concat_tables(tables)


def extract_lmsys_messages(row):
    """Convert LMSYS conversation to ChatML messages."""
    conv = row.get("conversation", [])
    if not conv:
        return None
    
    messages = []
    for turn in conv:
        if isinstance(turn, dict) and "role" in turn and "content" in turn:
            role = turn["role"]
            content = turn["content"]
            if role in ("user", "assistant") and content:
                messages.append({"role": role, "content": content})
    
    return messages if len(messages) >= 2 else None


def extract_magpie_messages(row):
    """Convert Magpie conversation to ChatML messages."""
    conv = row.get("conversations", [])
    if not conv:
        return None
    
    messages = []
    for turn in conv:
        if isinstance(turn, dict) and "from" in turn and "value" in turn:
            role = "user" if turn["from"] == "human" else "assistant"
            content = turn["value"]
            if content:
                messages.append({"role": role, "content": content})
    
    return messages if len(messages) >= 2 else None


def extract_prosocial_messages(row):
    """Convert Prosocial Dialog to ChatML messages."""
    # Prosocial has: context, response, safety_annotation, etc.
    context = row.get("context", "")
    response = row.get("response", "")
    
    if context and response:
        return [
            {"role": "user", "content": context},
            {"role": "assistant", "content": response}
        ]
    return None


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--lmsys-samples", type=int, default=50000)
    parser.add_argument("--magpie-samples", type=int, default=100000)
    parser.add_argument("--prosocial-samples", type=int, default=20000)
    parser.add_argument("--output", default="data/stage1_train.jsonl")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    
    random.seed(args.seed)
    base = Path(__file__).parent.parent / "datasets"
    
    all_conversations = []
    
    # 1. LMSYS-Chat-1M
    print("\n[1/3] Loading LMSYS-Chat-1M...")
    lmsys_cache = base / "lmsys-chat-1m/lmsys___lmsys-chat-1m/default/0.0.0/200748d9d3cddcc9d782887541057aca0b18c5da"
    lmsys_table = load_arrow_dataset(lmsys_cache)
    if lmsys_table:
        print(f"  Total: {len(lmsys_table)} rows")
        indices = random.sample(range(len(lmsys_table)), min(args.lmsys_samples, len(lmsys_table)))
        lmsys_count = 0
        for idx in indices:
            row = lmsys_table.slice(idx, 1).to_pydict()
            row = {k: v[0] for k, v in row.items()}
            msgs = extract_lmsys_messages(row)
            if msgs:
                all_conversations.append({"messages": msgs})
                lmsys_count += 1
        print(f"  Extracted: {lmsys_count} conversations")
    else:
        print("  ❌ Not found")
        lmsys_count = 0
    
    # 2. Magpie
    print("\n[2/3] Loading Magpie...")
    magpie_cache = base / "magpie/Magpie-Align___magpie-llama-3.1-pro-300_k-filtered/default/0.0.0/1a982eea9ece373700dd8dfd04a4de08c2578c24"
    magpie_table = load_arrow_dataset(magpie_cache)
    if magpie_table:
        print(f"  Total: {len(magpie_table)} rows")
        indices = random.sample(range(len(magpie_table)), min(args.magpie_samples, len(magpie_table)))
        magpie_count = 0
        for idx in indices:
            row = magpie_table.slice(idx, 1).to_pydict()
            row = {k: v[0] for k, v in row.items()}
            msgs = extract_magpie_messages(row)
            if msgs:
                all_conversations.append({"messages": msgs})
                magpie_count += 1
        print(f"  Extracted: {magpie_count} conversations")
    else:
        print("  ❌ Not found")
        magpie_count = 0
    
    # 3. Prosocial Dialog
    print("\n[3/3] Loading Prosocial Dialog...")
    prosocial_cache = base / "prosocial/allenai___prosocial-dialog/default/0.0.0/d77d7ad3c624c51030f2f32c83e892b3d620b3d4"
    prosocial_table = load_arrow_dataset(prosocial_cache)
    if prosocial_table:
        print(f"  Total: {len(prosocial_table)} rows")
        indices = random.sample(range(len(prosocial_table)), min(args.prosocial_samples, len(prosocial_table)))
        prosocial_count = 0
        for idx in indices:
            row = prosocial_table.slice(idx, 1).to_pydict()
            row = {k: v[0] for k, v in row.items()}
            msgs = extract_prosocial_messages(row)
            if msgs:
                all_conversations.append({"messages": msgs})
                prosocial_count += 1
        print(f"  Extracted: {prosocial_count} conversations")
    else:
        print("  ❌ Not found")
        prosocial_count = 0
    
    # Shuffle
    print(f"\n📊 Total: {len(all_conversations)} conversations")
    random.shuffle(all_conversations)
    
    # Write JSONL
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    with out_path.open("w", encoding="utf-8") as f:
        for conv in all_conversations:
            f.write(json.dumps(conv, ensure_ascii=False) + "\n")
    
    print(f"\n✅ Wrote {out_path}")
    print(f"\nBreakdown:")
    print(f"  LMSYS-Chat-1M: {lmsys_count}")
    print(f"  Magpie: {magpie_count}")
    print(f"  Prosocial: {prosocial_count}")
    
    # Sample
    if all_conversations:
        print(f"\nSample conversation:")
        sample = all_conversations[0]
        for msg in sample["messages"][:2]:
            print(f"  [{msg['role']}] {msg['content'][:100]}...")


if __name__ == "__main__":
    main()
