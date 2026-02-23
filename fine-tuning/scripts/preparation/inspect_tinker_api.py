#!/usr/bin/env python3
"""Quick script to inspect Tinker SDK API"""

import os
import tinker

# Initialize client
base_url = os.getenv("TINKER_API_BASE", "https://tinker.thinkingmachines.dev/services/tinker-prod")
api_key = os.getenv("TINKER_API_KEY")

if not api_key:
    print("Set TINKER_API_KEY first")
    exit(1)

client = tinker.ServiceClient(base_url=base_url, api_key=api_key)

print("=== ServiceClient Methods ===")
for m in sorted(dir(client)):
    if not m.startswith('_'):
        print(f"  {m}")

print("\n=== Creating LoRA Training Client ===")
training_client = client.create_lora_training_client(
    base_model="Qwen/Qwen3-8B",
    rank=16
)

print("=== LoRA Training Client Methods ===")
for m in sorted(dir(training_client)):
    if not m.startswith('_'):
        print(f"  {m}")

print("\n=== Creating Sampling Client ===")
sampling_client = client.create_sampling_client()

print("=== Sampling Client Methods ===")
for m in sorted(dir(sampling_client)):
    if not m.startswith('_'):
        print(f"  {m}")
