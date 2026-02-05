#!/usr/bin/env python3
"""
Prepare training data from a conversational dataset.
"""

import json
import argparse
from pathlib import Path
from datasets import load_dataset


def extract_messages(example):
    """Convert various dialog formats to OpenAI-style messages."""
    # Check for direct messages field
    if "messages" in example and isinstance(example["messages"], list):
        msgs = []
        for m in example["messages"]:
            role = m.get("role") or m.get("from") or m.get("speaker")
            content = m.get("content") or m.get("value") or m.get("text")
            if role and content:
                role = role.replace("human", "user").replace("gpt", "assistant")
                if role in {"user", "assistant", "system"}:
                    msgs.append({"role": role, "content": content})
        return msgs if len(msgs) >= 2 else None
    
    # Check for dialog/dialogue field
    for key in ("dialog", "dialogue", "conversation", "conversations"):
        if key in example and isinstance(example[key], list):
            msgs = []
            for turn in example[key]:
                # Try different field names
                role = turn.get("role") or turn.get("from") or turn.get("speaker")
                content = turn.get("content") or turn.get("value") or turn.get("text")
                
                if role and content:
                    # Normalize role names
                    if role.lower() in {"human", "user", "person"}:
                        role = "user"
                    elif role.lower() in {"assistant", "bot", "gpt", "system"}:
                        role = "assistant"
                    
                    msgs.append({"role": role, "content": content})
            
            return msgs if len(msgs) >= 2 else None
    
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="HuggingFaceH4/ultrachat_200k")
    parser.add_argument("--split", default="train_sft")
    parser.add_argument("--output", default="data/training_data.jsonl")
    parser.add_argument("--max-examples", type=int, default=None, help="Limit number of examples")
    args = parser.parse_args()
    
    print(f"Loading dataset: {args.dataset} (split: {args.split})")
    
    try:
        ds = load_dataset(args.dataset, split=args.split, trust_remote_code=True)
    except Exception as e:
        print(f"Failed to load dataset: {e}")
        print("\nTrying without trust_remote_code...")
        ds = load_dataset(args.dataset, split=args.split)
    
    print(f"Loaded {len(ds)} examples")
    
    # Create output directory
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert to JSONL
    count = 0
    with out_path.open("w", encoding="utf-8") as f:
        for i, example in enumerate(ds):
            if args.max_examples and i >= args.max_examples:
                break
            
            msgs = extract_messages(example)
            if not msgs:
                continue
            
            f.write(json.dumps({"messages": msgs}, ensure_ascii=False) + "\n")
            count += 1
            
            if count % 1000 == 0:
                print(f"Processed {count} examples...")
    
    print(f"\nWrote {count} conversations to {out_path}")
    print(f"Example format:")
    
    # Show first example
    with out_path.open("r") as f:
        first = json.loads(f.readline())
        print(json.dumps(first, indent=2))


if __name__ == "__main__":
    main()
