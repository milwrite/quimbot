#!/usr/bin/env python3
"""Quick inspection of dataset formats - load directly from HF."""

import json
from datasets import load_dataset


def inspect(name, dataset_id, split="train"):
    """Load and show first example."""
    print(f"\n{'='*60}")
    print(f"{name}")
    print('='*60)
    
    try:
        print("Loading...")
        ds = load_dataset(dataset_id, split=split, streaming=True)
        
        # Get first example
        first = next(iter(ds))
        print(f"\nFirst example structure:")
        print(json.dumps(first, indent=2, default=str)[:1000] + "...")
        
    except Exception as e:
        print(f"❌ Error: {e}")


# Test each dataset
inspect("LMSYS-Chat-1M", "lmsys/lmsys-chat-1m")
inspect("Magpie", "Magpie-Align/Magpie-Llama-3.1-Pro-300K-Filtered")
inspect("Prosocial Dialog", "allenai/prosocial-dialog")
