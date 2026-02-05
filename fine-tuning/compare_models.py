#!/usr/bin/env python3
"""
Compare base model vs LoRA-tuned model outputs.
Generates responses for test prompts from both models.
"""

import argparse
import json
from pathlib import Path

import tinker


# Sample test prompts for dialogue evaluation
DEFAULT_TEST_PROMPTS = [
    {
        "messages": [
            {"role": "user", "content": "Hello! How are you today?"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Can you explain what photosynthesis is in simple terms?"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "I'm feeling stressed about work. Any advice?"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What's the difference between HTTP and HTTPS?"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Tell me a short story about a robot learning to paint."}
        ]
    }
]


def generate_response(client, messages, max_tokens=150):
    """
    Generate a response using the Tinker client.
    Note: Actual API depends on Tinker SDK - this is a placeholder.
    """
    try:
        # Placeholder - check Tinker SDK docs for actual generation method
        # response = client.generate(messages=messages, max_tokens=max_tokens)
        # return response['content']
        return "[PLACEHOLDER: Tinker SDK generation method TBD]"
    except Exception as e:
        return f"[ERROR: {e}]"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-model", default="Qwen/Qwen3-8B", help="Base model name")
    parser.add_argument("--lora-checkpoint", default=None, help="Path to LoRA checkpoint (optional)")
    parser.add_argument("--test-prompts", default=None, help="Path to custom test prompts JSONL")
    parser.add_argument("--output", default="comparison_results.json", help="Output file for results")
    parser.add_argument("--max-tokens", type=int, default=150, help="Max tokens per response")
    args = parser.parse_args()

    base_url = os.getenv("TINKER_API_BASE", "https://tinker.thinkingmachines.dev/services/tinker-prod")
    api_key = os.getenv("TINKER_API_KEY")
    if not api_key:
        raise SystemExit("❌ Missing TINKER_API_KEY in environment")

    print(f"🔧 Initializing Tinker clients...")
    service_client = tinker.ServiceClient(base_url=base_url, api_key=api_key)
    
    # Load test prompts
    if args.test_prompts:
        test_prompts = []
        with open(args.test_prompts, "r") as f:
            for line in f:
                test_prompts.append(json.loads(line.strip()))
    else:
        test_prompts = DEFAULT_TEST_PROMPTS
    
    print(f"📝 Testing with {len(test_prompts)} prompts")
    
    results = []
    
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\n--- Prompt {i}/{len(test_prompts)} ---")
        print(f"User: {prompt['messages'][-1]['content']}")
        
        result = {
            "prompt": prompt,
            "base_response": None,
            "lora_response": None
        }
        
        # Generate base model response
        print("Generating base model response...")
        # TODO: Implement actual generation call
        result["base_response"] = "[Base model generation pending Tinker SDK docs]"
        print(f"Base: {result['base_response'][:100]}...")
        
        # Generate LoRA model response (if checkpoint provided)
        if args.lora_checkpoint:
            print("Generating LoRA model response...")
            # TODO: Load LoRA and generate
            result["lora_response"] = "[LoRA generation pending Tinker SDK docs]"
            print(f"LoRA: {result['lora_response'][:100]}...")
        
        results.append(result)
    
    # Save results
    output_path = Path(args.output)
    with output_path.open("w") as f:
        json.dump({
            "base_model": args.base_model,
            "lora_checkpoint": args.lora_checkpoint,
            "test_count": len(test_prompts),
            "results": results
        }, f, indent=2)
    
    print(f"\n✅ Results saved to {output_path}")
    print(f"\n📊 Summary:")
    print(f"   - Base model: {args.base_model}")
    print(f"   - LoRA checkpoint: {args.lora_checkpoint or 'None'}")
    print(f"   - Test prompts: {len(test_prompts)}")
    print(f"\nNext step: Review {output_path} to compare outputs")
    
    print("\n⚠️  NOTE: Generation methods are placeholders.")
    print("   Check Tinker SDK documentation for:")
    print("   - How to generate text with a model")
    print("   - How to load LoRA adapters for inference")
    print("   - Inference API endpoints/methods")


if __name__ == "__main__":
    import os
    main()
