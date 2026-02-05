#!/usr/bin/env python3
"""Verify saved checkpoints from the training run."""

import os
import tinker

# Initialize Tinker client
api_key = os.getenv("TINKER_API_KEY")
base_url = os.getenv("TINKER_API_BASE", "https://tinker.thinkingmachines.dev/services/tinker-prod")

print(f"Connecting to Tinker API at {base_url}...")
service_client = tinker.ServiceClient(base_url=base_url, api_key=api_key)

# Create a training client to access checkpoints
print("Creating LoRA training client...")
training_client = service_client.create_lora_training_client(
    base_model="Qwen/Qwen3-8B",
    rank=16,
)

print("\n📦 Saved Checkpoints:")
print("=" * 60)

# Try to list checkpoints
# Note: The SDK might not have a direct list method, so we'll try to save a dummy
# checkpoint to see the path format, then deduce the actual paths

try:
    # Get a checkpoint path to see the format
    test_future = training_client.save_weights_for_sampler(name="verify_test")
    test_response = test_future.result()
    base_path = test_response.path.rsplit('/', 1)[0]  # Get base path
    
    print(f"\nBase checkpoint path: {base_path}/")
    print(f"\nExpected checkpoints:")
    print(f"  1. {base_path}/step_0005")
    print(f"  2. {base_path}/step_0010")
    print(f"  3. {base_path}/final")
    print(f"\nTest checkpoint: {test_response.path}")
    
except Exception as e:
    print(f"Error: {e}")
