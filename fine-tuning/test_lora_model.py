#!/usr/bin/env python3
"""
Test LoRA-tuned model by generating responses to sample prompts.
Compares base model vs LoRA-tuned model outputs.
"""

import argparse
import json
import os
from pathlib import Path

import tinker


# Sample test prompts for dialogue evaluation
DEFAULT_TEST_PROMPTS = [
    [{"role": "user", "content": "Hello! How are you today?"}],
    [{"role": "user", "content": "Can you explain what photosynthesis is in simple terms?"}],
    [{"role": "user", "content": "I'm feeling stressed about work. Any advice?"}],
    [{"role": "user", "content": "What's the difference between HTTP and HTTPS?"}],
    [{"role": "user", "content": "Tell me a short story about a robot learning to paint."}],
]


def generate_text(sampling_client, prompt_messages, max_tokens=150, temperature=0.7):
    """
    Generate text using Tinker sampling client.
    """
    try:
        # Convert messages to tokens using chat template
        tokenizer = sampling_client.get_tokenizer()
        prompt_text = tokenizer.apply_chat_template(
            prompt_messages,
            tokenize=False,
            add_generation_prompt=True
        )
        
        # Tokenize
        input_ids = tokenizer.encode(prompt_text, add_special_tokens=False)
        
        # Sample from model
        # Note: Actual sampling API may differ - check Tinker docs
        result = sampling_client.sample(
            input_tokens=input_ids,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        # Decode response
        response_tokens = result.tokens if hasattr(result, 'tokens') else result
        response_text = tokenizer.decode(response_tokens, skip_special_tokens=True)
        
        return response_text
        
    except Exception as e:
        return f"[ERROR: {e}]"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-model", default="Qwen/Qwen3-8B", help="Base model name")
    parser.add_argument("--lora-weights", required=True, help="Path to saved LoRA weights")
    parser.add_argument("--test-prompts", default=None, help="Path to custom test prompts JSON")
    parser.add_argument("--output", default="lora_test_results.json", help="Output file")
    parser.add_argument("--max-tokens", type=int, default=150, help="Max tokens per response")
    parser.add_argument("--temperature", type=float, default=0.7, help="Sampling temperature")
    parser.add_argument("--compare-base", action="store_true", help="Also test base model for comparison")
    args = parser.parse_args()

    base_url = os.getenv("TINKER_API_BASE", "https://tinker.thinkingmachines.dev/services/tinker-prod")
    api_key = os.getenv("TINKER_API_KEY")
    if not api_key:
        raise SystemExit("❌ Missing TINKER_API_KEY in environment")

    print(f"🔧 Initializing Tinker clients...")
    service_client = tinker.ServiceClient(base_url=base_url, api_key=api_key)
    
    # Load test prompts
    if args.test_prompts:
        with open(args.test_prompts, "r") as f:
            test_prompts = json.load(f)
    else:
        test_prompts = DEFAULT_TEST_PROMPTS
    
    print(f"📝 Testing with {len(test_prompts)} prompts")
    
    # Create sampling client for LoRA model
    print(f"Loading LoRA weights from {args.lora_weights}...")
    lora_sampler = service_client.create_sampling_client(
        base_model=args.base_model,
        model_path=args.lora_weights
    )
    print("✅ LoRA sampling client ready")
    
    # Create base model sampler if comparison requested
    base_sampler = None
    if args.compare_base:
        print(f"Loading base model {args.base_model}...")
        base_sampler = service_client.create_sampling_client(
            base_model=args.base_model
        )
        print("✅ Base model sampling client ready")
    
    results = []
    
    for i, prompt_messages in enumerate(test_prompts, 1):
        print(f"\n{'='*60}")
        print(f"Prompt {i}/{len(test_prompts)}")
        print(f"{'='*60}")
        print(f"User: {prompt_messages[-1]['content']}")
        print()
        
        result = {
            "prompt": prompt_messages,
            "lora_response": None,
            "base_response": None
        }
        
        # Generate LoRA response
        print("🤖 LoRA Model:")
        lora_response = generate_text(
            lora_sampler,
            prompt_messages,
            max_tokens=args.max_tokens,
            temperature=args.temperature
        )
        result["lora_response"] = lora_response
        print(lora_response)
        print()
        
        # Generate base model response if requested
        if base_sampler:
            print("🤖 Base Model:")
            base_response = generate_text(
                base_sampler,
                prompt_messages,
                max_tokens=args.max_tokens,
                temperature=args.temperature
            )
            result["base_response"] = base_response
            print(base_response)
            print()
        
        results.append(result)
    
    # Save results
    output_path = Path(args.output)
    with output_path.open("w") as f:
        json.dump({
            "base_model": args.base_model,
            "lora_weights": args.lora_weights,
            "test_count": len(test_prompts),
            "max_tokens": args.max_tokens,
            "temperature": args.temperature,
            "results": results
        }, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"✅ Results saved to {output_path}")
    print(f"{'='*60}")
    print(f"\n📊 Summary:")
    print(f"   - Base model: {args.base_model}")
    print(f"   - LoRA weights: {args.lora_weights}")
    print(f"   - Test prompts: {len(test_prompts)}")
    print(f"   - Temperature: {args.temperature}")
    print(f"   - Max tokens: {args.max_tokens}")


if __name__ == "__main__":
    main()
