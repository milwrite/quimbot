#!/usr/bin/env python3
"""
Run LoRA fine-tuning via Tinker SDK using chat JSONL data.
Uses HF chat template via tokenizer.apply_chat_template to build prompt/completion
and masks loss to only the final assistant message.
"""

import argparse
import json
import os
from pathlib import Path

import tinker
from tinker import types


def iter_jsonl(path: Path):
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def build_datum(messages, tokenizer):
    if not messages or messages[-1].get("role") != "assistant":
        return None

    # prompt up to assistant start
    prompt_messages = messages[:-1]
    prompt_str = tokenizer.apply_chat_template(
        prompt_messages,
        tokenize=False,
        add_generation_prompt=True,
    )
    full_str = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=False,
    )

    prompt_tokens = tokenizer.encode(prompt_str, add_special_tokens=False)
    full_tokens = tokenizer.encode(full_str, add_special_tokens=False)

    if len(full_tokens) <= len(prompt_tokens):
        return None

    weights = [0] * len(prompt_tokens) + [1] * (len(full_tokens) - len(prompt_tokens))

    input_tokens = full_tokens[:-1]
    target_tokens = full_tokens[1:]
    weights = weights[1:]

    return types.Datum(
        model_input=types.ModelInput.from_ints(tokens=input_tokens),
        loss_fn_inputs=dict(weights=weights, target_tokens=target_tokens),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to JSONL with OpenAI-style messages")
    parser.add_argument("--base-model", default=None, help="Tinker base model name")
    parser.add_argument("--rank", type=int, default=16, help="LoRA rank")
    parser.add_argument("--learning-rate", type=float, default=1e-4)
    parser.add_argument("--batch", type=int, default=64)
    parser.add_argument("--max-steps", type=int, default=0, help="0=full epoch")
    args = parser.parse_args()

    base_url = os.getenv("TINKER_API_BASE", "https://tinker.thinkingmachines.dev/services/tinker-prod")
    api_key = os.getenv("TINKER_API_KEY")
    if not api_key:
        raise SystemExit("❌ Missing TINKER_API_KEY in environment")

    print(f"Initializing Tinker ServiceClient (base_url={base_url})")
    service_client = tinker.ServiceClient(base_url=base_url, api_key=api_key)
    print("✓ ServiceClient initialized")
    
    print("Getting server capabilities...")
    caps = service_client.get_server_capabilities()
    models = [m.model_name for m in caps.supported_models]
    print(f"✓ Available models: {models}")

    if args.base_model is None:
        # pick first Qwen 8B-ish model if available
        qwen_8b = [m for m in models if "Qwen" in m and ("8B" in m or "8b" in m)]
        if not qwen_8b:
            raise SystemExit("No Qwen 8B model found. Pass --base-model explicitly.")
        base_model = qwen_8b[0]
        print(f"✓ Auto-selected base model: {base_model}")
    else:
        base_model = args.base_model
        print(f"✓ Using base model: {base_model}")

    print(f"Creating LoRA training client (rank={args.rank})...")
    training_client = service_client.create_lora_training_client(
        base_model=base_model,
        rank=args.rank,
    )
    print("✓ Training client created")

    print("Getting tokenizer...")
    tokenizer = training_client.get_tokenizer()
    print("✓ Tokenizer ready")

    data_path = Path(args.data)
    print(f"Loading data from {data_path}...")
    batch = []
    step = 0

    for ex in iter_jsonl(data_path):
        msgs = ex.get("messages")
        if not isinstance(msgs, list):
            continue
        datum = build_datum(msgs, tokenizer)
        if not datum:
            continue
        batch.append(datum)

        if len(batch) >= args.batch:
            print(f"Step {step + 1}: Training on batch of {len(batch)} examples...")
            fwdbwd = training_client.forward_backward(batch, "cross_entropy")
            optim = training_client.optim_step(types.AdamParams(learning_rate=args.learning_rate))
            fwd_result = fwdbwd.result()
            opt_result = optim.result()
            print(f"✓ Step {step + 1} complete")
            batch = []
            step += 1
            if args.max_steps and step >= args.max_steps:
                print(f"Reached max_steps={args.max_steps}, stopping")
                break

    if batch:
        print(f"Final batch: Training on {len(batch)} examples...")
        fwdbwd = training_client.forward_backward(batch, "cross_entropy")
        optim = training_client.optim_step(types.AdamParams(learning_rate=args.learning_rate))
        fwdbwd.result(); optim.result()
        print("✓ Final batch complete")

    print(f"\n✅ Training complete! Total steps: {step}")


if __name__ == "__main__":
    main()
