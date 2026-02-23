#!/usr/bin/env python3
"""
Prepare multi-dataset training data combining:
1. LMSYS-Chat-1M (real user conversations)
2. Magpie-Llama-3.1-Pro-300K-Filtered (synthetic)
3. AllenAI Prosocial Dialog (safety)
4. WAXAL Stage2 variants (African languages)
"""

import json
import argparse
from pathlib import Path
from datasets import load_dataset, load_from_disk
import random


def extract_messages_lmsys(example):
    """Convert LMSYS format to messages."""
    # LMSYS has 'conversation' field with 'content' list
    if "conversation" in example:
        msgs = []
        for turn in example["conversation"]:
            if isinstance(turn, dict) and "content" in turn and "role" in turn:
                role = turn["role"]
                if role == "user" or role == "assistant":
                    msgs.append({"role": role, "content": turn["content"]})
        return msgs if len(msgs) >= 2 else None
    return None


def extract_messages_magpie(example):
    """Convert Magpie format to messages."""
    if "conversations" in example:
        msgs = []
        for turn in example["conversations"]:
            if "from" in turn and "value" in turn:
                role = "user" if turn["from"] == "human" else "assistant"
                msgs.append({"role": role, "content": turn["value"]})
        return msgs if len(msgs) >= 2 else None
    return None


def extract_messages_prosocial(example):
    """Convert Prosocial Dialog format to messages."""
    if "dialogue" in example:
        msgs = []
        for turn in example["dialogue"]:
            if "text" in turn and "speaker" in turn:
                role = "user" if turn["speaker"] == "USER" else "assistant"
                msgs.append({"role": role, "content": turn["text"]})
        return msgs if len(msgs) >= 2 else None
    return None


def extract_messages_waxal(example):
    """Convert WAXAL format to messages (TTS data - may need adaptation)."""
    # WAXAL is primarily TTS data; check actual format
    if "text" in example:
        # Create simple Q&A from text (adapt as needed)
        return [
            {"role": "user", "content": f"Translate or explain: {example['text']}"},
            {"role": "assistant", "content": example['text']}
        ]
    return None


def load_and_convert(dataset_name, loader_fn, extractor_fn, max_examples=None, cache_dir=None):
    """Load dataset and convert to messages format."""
    print(f"\nLoading {dataset_name}...")
    
    try:
        if cache_dir and Path(cache_dir).exists():
            # Try loading from local cache first
            ds = load_from_disk(cache_dir)
            print(f"  Loaded from cache: {cache_dir}")
        else:
            ds = loader_fn()
            print(f"  Loaded from HuggingFace")
        
        print(f"  Total examples: {len(ds)}")
        
        # Convert to messages
        messages_list = []
        for i, example in enumerate(ds):
            if max_examples and i >= max_examples:
                break
            
            msgs = extractor_fn(example)
            if msgs:
                messages_list.append({"messages": msgs})
            
            if (i + 1) % 10000 == 0:
                print(f"  Processed {i + 1} examples...")
        
        print(f"  Converted {len(messages_list)} valid conversations")
        return messages_list
    
    except Exception as e:
        print(f"  ❌ Error loading {dataset_name}: {e}")
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="data/multi_dataset_train.jsonl")
    parser.add_argument("--lmsys-samples", type=int, default=50000, 
                        help="Sample N examples from LMSYS-Chat-1M (default: 50k)")
    parser.add_argument("--magpie-samples", type=int, default=100000,
                        help="Sample N examples from Magpie (default: 100k)")
    parser.add_argument("--prosocial-samples", type=int, default=20000,
                        help="Sample N examples from Prosocial (default: 20k)")
    parser.add_argument("--waxal-samples", type=int, default=10000,
                        help="Sample N examples from WAXAL (default: 10k)")
    parser.add_argument("--shuffle", action="store_true",
                        help="Shuffle final dataset")
    args = parser.parse_args()
    
    # Create output directory
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    
    all_messages = []
    
    # 1. LMSYS-Chat-1M (real conversations)
    lmsys_data = load_and_convert(
        "LMSYS-Chat-1M",
        lambda: load_dataset("lmsys/lmsys-chat-1m", split="train"),
        extract_messages_lmsys,
        max_examples=args.lmsys_samples,
        cache_dir="../datasets/lmsys-chat-1m/lmsys___lmsys-chat-1m/default/0.0.0/200748d9d3cddcc9d782887541057aca0b18c5da"
    )
    all_messages.extend(lmsys_data)
    
    # 2. Magpie (synthetic high-quality)
    magpie_data = load_and_convert(
        "Magpie-Llama-3.1-Pro-300K-Filtered",
        lambda: load_dataset("Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered", split="train"),
        extract_messages_magpie,
        max_examples=args.magpie_samples,
        cache_dir="../datasets/magpie/Magpie-Align___magpie-llama-3.1-pro-300_k-filtered"
    )
    all_messages.extend(magpie_data)
    
    # 3. Prosocial Dialog (safety)
    prosocial_data = load_and_convert(
        "AllenAI Prosocial Dialog",
        lambda: load_dataset("allenai/prosocial-dialog", split="train"),
        extract_messages_prosocial,
        max_examples=args.prosocial_samples,
        cache_dir="../datasets/prosocial/allenai___prosocial-dialog"
    )
    all_messages.extend(prosocial_data)
    
    # 4. WAXAL Stage2 (African languages)
    # Note: May need to adjust loader based on actual WAXAL format
    print("\n⚠️  WAXAL integration pending - checking dataset format...")
    print("   Skipping WAXAL for now (add after format verification)")
    
    # Shuffle if requested
    if args.shuffle:
        print(f"\nShuffling {len(all_messages)} conversations...")
        random.shuffle(all_messages)
    
    # Write to JSONL
    print(f"\nWriting to {out_path}...")
    with out_path.open("w", encoding="utf-8") as f:
        for item in all_messages:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    
    print(f"\n✅ Complete! Wrote {len(all_messages)} conversations")
    print(f"\nDataset breakdown:")
    print(f"  LMSYS-Chat-1M: {len(lmsys_data)} examples")
    print(f"  Magpie: {len(magpie_data)} examples")
    print(f"  Prosocial: {len(prosocial_data)} examples")
    print(f"  WAXAL: 0 examples (pending)")
    
    # Show example
    print(f"\nExample conversation:")
    if all_messages:
        print(json.dumps(all_messages[0], indent=2))


if __name__ == "__main__":
    main()
