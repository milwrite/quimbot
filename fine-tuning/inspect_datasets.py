#!/usr/bin/env python3
"""Quick inspection of dataset formats."""

import json
from datasets import load_dataset, load_from_disk
from pathlib import Path


def inspect_dataset(name, loader_fn, cache_dir=None):
    """Load and show first example."""
    print(f"\n{'='*60}")
    print(f"Dataset: {name}")
    print('='*60)
    
    try:
        if cache_dir and Path(cache_dir).exists():
            ds = load_from_disk(cache_dir)
        else:
            ds = loader_fn()
        
        print(f"Size: {len(ds)} examples")
        print(f"Features: {ds.features}")
        print(f"\nFirst example:")
        print(json.dumps(ds[0], indent=2, default=str))
        
    except Exception as e:
        print(f"❌ Error: {e}")


# 1. LMSYS-Chat-1M
inspect_dataset(
    "LMSYS-Chat-1M",
    lambda: load_dataset("lmsys/lmsys-chat-1m", split="train"),
    "../datasets/lmsys-chat-1m/lmsys___lmsys-chat-1m/default/0.0.0/200748d9d3cddcc9d782887541057aca0b18c5da"
)

# 2. Magpie
inspect_dataset(
    "Magpie-Llama-3.1-Pro-300K-Filtered",
    lambda: load_dataset("Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered", split="train"),
    "../datasets/magpie/Magpie-Align___magpie-llama-3.1-pro-300_k-filtered/default/0.0.0"
)

# 3. Prosocial
inspect_dataset(
    "AllenAI Prosocial Dialog",
    lambda: load_dataset("allenai/prosocial-dialog", split="train"),
    "../datasets/prosocial/allenai___prosocial-dialog/default/0.0.0"
)

# 4. WAXAL
print("\n" + "="*60)
print("WAXAL Stage2 Variants")
print("="*60)
waxal_dir = Path("../datasets/stage2-variants/waxal")
if waxal_dir.exists():
    print(f"Directory contents:")
    for item in waxal_dir.iterdir():
        print(f"  {item.name}")
else:
    print("❌ Not found")
