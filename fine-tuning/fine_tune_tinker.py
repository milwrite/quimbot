#!/usr/bin/env python3
"""
Fine-tune via Tinker API using a Hugging Face dialog dataset.
Defaults:
- Dataset: HuggingFaceH4/ultrachat_200k (train)
- Model suffix: qwen-8b-dialog

Assumes an OpenAI-compatible Tinker API:
- POST /files (multipart) with purpose=fine-tune
- POST /fine-tunes with training_file + model
"""

import argparse
import json
import os
from pathlib import Path

import requests
from datasets import load_dataset
from dotenv import load_dotenv


def extract_messages(example):
    """Convert common dialog formats to OpenAI-style messages.
    Returns list[dict] with keys role/content or None if unsupported.
    """
    if "messages" in example and isinstance(example["messages"], list):
        msgs = []
        for m in example["messages"]:
            role = m.get("role") or m.get("from") or m.get("speaker")
            content = m.get("content") or m.get("value") or m.get("text")
            if role and content:
                role = role.replace("human", "user").replace("assistant", "assistant")
                if role in {"user", "assistant", "system"}:
                    msgs.append({"role": role, "content": content})
        return msgs if len(msgs) >= 2 else None

    # ShareGPT-style
    if "conversations" in example and isinstance(example["conversations"], list):
        msgs = []
        for m in example["conversations"]:
            role = m.get("from") or m.get("role")
            content = m.get("value") or m.get("content")
            if role and content:
                role = "assistant" if role.lower() in {"gpt", "assistant"} else "user"
                msgs.append({"role": role, "content": content})
        return msgs if len(msgs) >= 2 else None

    # Generic dialog field
    for key in ("dialog", "dialogue", "conversation", "chat"):
        if key in example and isinstance(example[key], list):
            msgs = []
            for m in example[key]:
                role = m.get("role") or m.get("speaker") or m.get("from")
                content = m.get("content") or m.get("text") or m.get("value")
                if role and content:
                    role = "assistant" if role.lower() in {"assistant", "bot", "gpt"} else "user"
                    msgs.append({"role": role, "content": content})
            return msgs if len(msgs) >= 2 else None

    return None


def build_jsonl(dataset_name, split, out_path):
    ds = load_dataset(dataset_name, split=split)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    with out_path.open("w", encoding="utf-8") as f:
        for ex in ds:
            msgs = extract_messages(ex)
            if not msgs:
                continue
            f.write(json.dumps({"messages": msgs}, ensure_ascii=False) + "\n")
            count += 1
    return count


def tinker_upload_file(api_base, api_key, jsonl_path):
    url = f"{api_base}/files"
    with open(jsonl_path, "rb") as fh:
        files = {"file": fh}
        data = {"purpose": "fine-tune"}
        headers = {"Authorization": f"Bearer {api_key}"}
        r = requests.post(url, headers=headers, data=data, files=files, timeout=600)
        r.raise_for_status()
        return r.json()["id"]


def tinker_fine_tune(api_base, api_key, training_file_id, model_suffix):
    url = f"{api_base}/fine-tunes"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    payload = {
        "training_file": training_file_id,
        "model": "qwen-8b",
        "suffix": model_suffix,
    }
    r = requests.post(url, headers=headers, json=payload, timeout=600)
    r.raise_for_status()
    return r.json()


def main():
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", default="HuggingFaceH4/ultrachat_200k")
    parser.add_argument("--split", default="train_sft")
    parser.add_argument("--model", default="qwen-8b-dialog")
    parser.add_argument("--out", default="data/ultrachat_200k_train_sft.jsonl")
    parser.add_argument("--no-upload", action="store_true", help="Only build JSONL, skip API calls")
    args = parser.parse_args()

    api_key = os.getenv("TINKER_API_KEY")
    api_base = os.getenv("TINKER_API_BASE", "https://api.tinker.ai/v1")

    out_path = Path(args.out)
    count = build_jsonl(args.dataset, args.split, out_path)
    print(f"Wrote {count} examples to {out_path}")

    if args.no_upload:
        return

    if not api_key:
        raise SystemExit("Missing TINKER_API_KEY in environment")

    file_id = tinker_upload_file(api_base, api_key, out_path)
    print(f"Uploaded training file: {file_id}")

    job = tinker_fine_tune(api_base, api_key, file_id, args.model)
    print("Fine-tune job:")
    print(json.dumps(job, indent=2))


if __name__ == "__main__":
    main()
