#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qwen Model Evaluation Script
Compare base model vs fine-tuned variants for pedagogical dialogue quality.

Usage:
    python qwen-eval.py --models qwen2.5:8b qwen-8b-dialog-v1 --output results.json
    python qwen-eval.py --test-suite pedagogical --verbose
"""

import json
import subprocess
import sys
import time
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any
import argparse


@dataclass
class EvalResult:
    """Single model evaluation result"""
    model: str
    prompt: str
    response: str
    tokens_per_sec: float
    total_time: float
    timestamp: str


# Test suites for different evaluation scenarios
TEST_SUITES = {
    "pedagogical": [
        {
            "name": "scaffolding_inquiry",
            "prompt": "I'm struggling to understand why photosynthesis requires light. Can you help?",
            "criteria": "Should ask questions, scaffold thinking, avoid direct answers"
        },
        {
            "name": "adaptive_depth",
            "prompt": "What's a derivative in calculus?",
            "criteria": "Should probe understanding level before explaining"
        },
        {
            "name": "socratic_method",
            "prompt": "Tell me how to solve 2x + 5 = 13",
            "criteria": "Should guide through questions rather than showing steps"
        },
        {
            "name": "metacognitive",
            "prompt": "I don't know how to start writing this essay about climate change.",
            "criteria": "Should help identify what they DO know, guide process"
        }
    ],
    "dialogue": [
        {
            "name": "multi_turn_context",
            "prompt": "I want to learn Python but I've never programmed before.",
            "criteria": "Should establish context through questions"
        },
        {
            "name": "collaborative",
            "prompt": "Can you explain how neural networks work?",
            "criteria": "Should invite co-investigation, not lecture"
        }
    ],
    "baseline": [
        {
            "name": "factual_recall",
            "prompt": "What is the capital of France?",
            "criteria": "Simple factual answer"
        },
        {
            "name": "basic_instruction",
            "prompt": "How do I make a list in Python?",
            "criteria": "Clear technical explanation"
        }
    ]
}


def run_ollama_inference(model: str, prompt: str, timeout: int = 60) -> Dict[str, Any]:
    """
    Run inference with an Ollama model and capture timing.
    
    Returns:
        dict with 'response', 'time', 'tokens_per_sec'
    """
    start = time.time()
    
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            capture_output=True,
            text=True,
            timeout=timeout
        )
        
        elapsed = time.time() - start
        
        if result.returncode != 0:
            return {
                "response": f"ERROR: {result.stderr}",
                "time": elapsed,
                "tokens_per_sec": 0
            }
        
        response = result.stdout.strip()
        
        # Rough token estimation (words * 1.3)
        estimated_tokens = len(response.split()) * 1.3
        tokens_per_sec = estimated_tokens / elapsed if elapsed > 0 else 0
        
        return {
            "response": response,
            "time": elapsed,
            "tokens_per_sec": tokens_per_sec
        }
        
    except subprocess.TimeoutExpired:
        return {
            "response": "ERROR: Timeout",
            "time": timeout,
            "tokens_per_sec": 0
        }
    except Exception as e:
        return {
            "response": f"ERROR: {str(e)}",
            "time": 0,
            "tokens_per_sec": 0
        }


def evaluate_models(models: List[str], test_suite: str = "pedagogical", verbose: bool = False) -> List[EvalResult]:
    """
    Evaluate multiple models against a test suite.
    
    Args:
        models: List of model names (ollama format)
        test_suite: Which test suite to use
        verbose: Print progress
        
    Returns:
        List of EvalResult objects
    """
    results = []
    tests = TEST_SUITES.get(test_suite, TEST_SUITES["pedagogical"])
    
    for model in models:
        if verbose:
            print(f"\n{'='*60}")
            print(f"Evaluating: {model}")
            print(f"{'='*60}")
        
        for test in tests:
            if verbose:
                print(f"\n[{test['name']}]")
                print(f"Prompt: {test['prompt']}")
                print(f"Criteria: {test['criteria']}")
                print("\nRunning inference...")
            
            inference = run_ollama_inference(model, test['prompt'])
            
            result = EvalResult(
                model=model,
                prompt=test['prompt'],
                response=inference['response'],
                tokens_per_sec=inference['tokens_per_sec'],
                total_time=inference['time'],
                timestamp=datetime.now().isoformat()
            )
            
            results.append(result)
            
            if verbose:
                print(f"\n→ Response ({inference['time']:.2f}s, {inference['tokens_per_sec']:.1f} tok/s):")
                print(f"{inference['response'][:500]}...")
    
    return results


def compare_side_by_side(results: List[EvalResult], prompt: str) -> str:
    """Generate side-by-side comparison for a specific prompt"""
    relevant = [r for r in results if r.prompt == prompt]
    
    output = [f"\n{'='*80}"]
    output.append(f"PROMPT: {prompt}")
    output.append('='*80)
    
    for r in relevant:
        output.append(f"\n[{r.model}] ({r.total_time:.2f}s, {r.tokens_per_sec:.1f} tok/s)")
        output.append("-" * 80)
        output.append(r.response)
        output.append("")
    
    return "\n".join(output)


def generate_report(results: List[EvalResult], output_path: Path = None) -> str:
    """Generate markdown evaluation report"""
    
    report = ["# Qwen Model Evaluation Report", ""]
    report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    
    # Group by model
    models = list(set(r.model for r in results))
    report.append(f"**Models evaluated:** {', '.join(models)}")
    report.append("")
    
    # Performance summary
    report.append("## Performance Summary")
    report.append("")
    report.append("| Model | Avg Time (s) | Avg Speed (tok/s) |")
    report.append("|-------|--------------|-------------------|")
    
    for model in models:
        model_results = [r for r in results if r.model == model]
        avg_time = sum(r.total_time for r in model_results) / len(model_results)
        avg_speed = sum(r.tokens_per_sec for r in model_results) / len(model_results)
        report.append(f"| {model} | {avg_time:.2f} | {avg_speed:.1f} |")
    
    report.append("")
    
    # Detailed comparisons
    report.append("## Response Comparisons")
    report.append("")
    
    prompts = list(set(r.prompt for r in results))
    
    for prompt in prompts:
        report.append(f"### Prompt: {prompt}")
        report.append("")
        
        for model in models:
            result = next((r for r in results if r.model == model and r.prompt == prompt), None)
            if result:
                report.append(f"#### {model}")
                report.append(f"*Time: {result.total_time:.2f}s | Speed: {result.tokens_per_sec:.1f} tok/s*")
                report.append("")
                report.append(result.response)
                report.append("")
    
    report_text = "\n".join(report)
    
    if output_path:
        output_path.write_text(report_text)
        print(f"\n✓ Report saved to: {output_path}")
    
    return report_text


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate Qwen model variants for pedagogical dialogue"
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=["qwen2.5:8b", "qwen-8b-dialog-v1"],
        help="Model names to evaluate (default: base + dialog-v1)"
    )
    parser.add_argument(
        "--test-suite",
        choices=list(TEST_SUITES.keys()),
        default="pedagogical",
        help="Which test suite to run"
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output path for results (JSON)"
    )
    parser.add_argument(
        "--report",
        type=Path,
        help="Output path for markdown report"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print detailed progress"
    )
    parser.add_argument(
        "--list-suites",
        action="store_true",
        help="List available test suites and exit"
    )
    
    args = parser.parse_args()
    
    if args.list_suites:
        print("\nAvailable test suites:")
        for name, tests in TEST_SUITES.items():
            print(f"\n{name}:")
            for test in tests:
                print(f"  - {test['name']}: {test['criteria']}")
        sys.exit(0)
    
    print(f"\n🔬 Qwen Model Evaluation")
    print(f"Models: {', '.join(args.models)}")
    print(f"Test Suite: {args.test_suite}")
    print(f"Tests: {len(TEST_SUITES[args.test_suite])}")
    
    # Run evaluation
    results = evaluate_models(
        models=args.models,
        test_suite=args.test_suite,
        verbose=args.verbose
    )
    
    # Save JSON results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump([asdict(r) for r in results], f, indent=2)
        print(f"\n✓ Results saved to: {args.output}")
    
    # Generate report
    report_path = args.report or Path("qwen-eval-report.md")
    generate_report(results, report_path)
    
    print("\n✅ Evaluation complete!")


if __name__ == "__main__":
    main()
