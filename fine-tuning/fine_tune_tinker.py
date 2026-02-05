#!/usr/bin/env python3
"""
Fine-tune via Tinker Python SDK (ServiceClient + TrainingClient).
Defaults:
- Dataset JSONL: /home/milwrite/molt/ultrachat_200k_train_sft.jsonl
- Base model: Qwen/Qwen3-8B
- Model suffix: qwen-8b-dialog

This uses the tinker-cookbook utilities to render chat messages into
Tinker Datums and runs a simple supervised training loop.
"""

import argparse
import os
import time
from pathlib import Path

from dotenv import load_dotenv
import datasets
import tinker
from tinker_cookbook import model_info, renderers
from tinker_cookbook.supervised.common import compute_mean_nll
from tinker_cookbook.supervised.data import conversation_to_datum
from tinker_cookbook.tokenizer_utils import get_tokenizer


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="/home/milwrite/molt/ultrachat_200k_train_sft.jsonl")
    parser.add_argument("--base-model", default="Qwen/Qwen3-8B")
    parser.add_argument("--suffix", default="qwen-8b-dialog")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=1e-4)
    parser.add_argument("--max-length", type=int, default=8192)
    parser.add_argument("--lora-rank", type=int, default=32)
    parser.add_argument("--steps", type=int, default=200)
    parser.add_argument("--base-url", default=os.getenv("TINKER_API_BASE", "https://tinker.thinkingmachines.dev/services/tinker-prod"))
    args = parser.parse_args()

    api_key = os.getenv("TINKER_API_KEY")
    if not api_key:
        raise SystemExit("Missing TINKER_API_KEY in environment")

    data_path = Path(args.data)
    if not data_path.exists():
        raise SystemExit(f"Dataset not found: {data_path}")

    # Load dataset from JSONL
    ds = datasets.load_dataset("json", data_files=str(data_path), split="train")

    # Renderer + tokenizer for the base model
    tokenizer = get_tokenizer(args.base_model)
    renderer_name = model_info.get_recommended_renderer_name(args.base_model)
    renderer = renderers.get_renderer(renderer_name, tokenizer)

    # Tinker client
    print(f"Initializing Tinker ServiceClient (base_url={args.base_url})")
    service_client = tinker.ServiceClient(base_url=args.base_url, api_key=api_key)
    print("Creating LoRA training client...")
    training_client = service_client.create_lora_training_client(
        base_model=args.base_model,
        rank=args.lora_rank,
        user_metadata={"suffix": args.suffix},
    )
    print("Training client ready.")

    # Shuffle once
    ds = ds.shuffle(seed=0)

    n_batches = max(1, len(ds) // args.batch_size)
    steps = min(args.steps, n_batches)

    print(f"Training for {steps} steps (batch_size={args.batch_size})")

    for step in range(steps):
        start = step * args.batch_size
        end = min((step + 1) * args.batch_size, len(ds))
        batch_rows = ds.select(range(start, end))

        batch = [
            conversation_to_datum(
                row["messages"],
                renderer,
                args.max_length,
                renderers.TrainOnWhat.ALL_ASSISTANT_MESSAGES,
            )
            for row in batch_rows
        ]

        # Linear LR decay
        lr_mult = max(0.0, 1.0 - step / steps)
        current_lr = args.learning_rate * lr_mult
        adam_params = tinker.AdamParams(
            learning_rate=current_lr, beta1=0.9, beta2=0.95, eps=1e-8
        )

        fwd_bwd_future = training_client.forward_backward(batch, loss_fn="cross_entropy")
        optim_future = training_client.optim_step(adam_params)

        fwd_bwd_result = fwd_bwd_future.result()
        optim_result = optim_future.result()

        train_logprobs = [x["logprobs"] for x in fwd_bwd_result.loss_fn_outputs]
        train_weights = [d.loss_fn_inputs["weights"] for d in batch]
        train_nll = compute_mean_nll(train_logprobs, train_weights)

        metrics = optim_result.metrics or {}
        metrics.update(
            step=step,
            num_sequences=len(batch),
            num_tokens=sum(d.model_input.length for d in batch),
            learning_rate=current_lr,
            train_nll=train_nll,
        )

        print(metrics)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
