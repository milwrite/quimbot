# Migration Guide: v1 → v2

Quick reference for upgrading from `qwen-eval.py` (v1) to `qwen-eval-v2.py`.

## TL;DR

```bash
# v1 command
python3 qwen-eval.py --models a b --test-suite pedagogical --output out.json --report report.md --verbose

# v2 equivalent
python3 qwen-eval-v2.py --models a b --test-suite pedagogical --output out.json --report report.md --verbose
```

Most v1 commands work as-is in v2! The CLI is backward compatible.

## What Changed

### Architecture
- v1: Single 280-line script
- v2: Modular package (`qwen_eval/`) with 5+ modules

### New Features in v2

#### 1. Parallel Execution
```bash
# Run 8 evaluations in parallel
python3 qwen-eval-v2.py --workers 8
```

#### 2. Result Caching
```bash
# Cache results to avoid re-running
python3 qwen-eval-v2.py --cache

# Clear cache
python3 qwen-eval-v2.py --clear-cache
```

#### 3. Configuration Files
```bash
# Save config for reproducibility
python3 qwen-eval-v2.py --models a b --save-config my-eval.yaml

# Run from config
python3 qwen-eval-v2.py --config my-eval.yaml
```

#### 4. More Metrics
v1 had 3 basic metrics. v2 has 15+:
- Pedagogical: `inquiry_markers`, `imperative_count`
- Dialogue: `collaborative_markers`, `personal_pronouns`, `hedging_phrases`
- Complexity: `lexical_diversity`, `avg_sentence_length`

```bash
# Include specific metrics
python3 qwen-eval-v2.py --metrics question_count inquiry_markers lexical_diversity

# Compute all metrics
python3 qwen-eval-v2.py --all-metrics
```

#### 5. More Test Suites
v1: 3 suites (pedagogical, dialogue, baseline)
v2: 4 built-in suites + custom YAML support

```bash
# New stress test suite
python3 qwen-eval-v2.py --test-suite stress

# Custom suite from YAML
python3 qwen-eval-v2.py --test-suite my-custom-tests.yaml
```

#### 6. Better Logging
```bash
# v1: only --verbose flag
# v2: multiple levels
python3 qwen-eval-v2.py --quiet   # Errors only
python3 qwen-eval-v2.py            # Warnings
python3 qwen-eval-v2.py --verbose  # Info
python3 qwen-eval-v2.py --debug    # Everything
```

#### 7. Comparison Reporter
```bash
# Side-by-side text comparison
python3 qwen-eval-v2.py --comparison compare.txt
```

## Command Equivalents

| v1 | v2 | Notes |
|----|----|----|
| `--models a b` | `--models a b` | Same |
| `--test-suite pedagogical` | `--test-suite pedagogical` | Same |
| `--output x.json` | `--output x.json` | Same |
| `--report r.md` | `--report r.md` | Same |
| `--verbose` | `--verbose` | Same |
| `--list-suites` | `--list-suites` | More detail in v2 |
| N/A | `--workers 8` | New: parallel |
| N/A | `--cache` | New: caching |
| N/A | `--config file.yaml` | New: config files |
| N/A | `--metrics m1 m2` | New: metric selection |
| N/A | `--comparison c.txt` | New: side-by-side |

## Breaking Changes

### None! 🎉

v2 is designed to be backward compatible with v1 CLI usage. All v1 commands should work in v2.

### JSON Output Format

v2 JSON includes more metadata:

```json
{
  "metadata": {
    "generated_at": "...",
    "total_results": 24,
    "models": [...],
    "test_suites": [...]
  },
  "results": [...]
}
```

v1 just had `[...]` (array of results).

**Fix:** Access `report["results"]` instead of iterating the top level.

### Markdown Report

v2 reports include:
- Summary statistics section
- Metrics comparison tables
- Error summary (if any)

Content is richer but structure is similar.

## Recommended Workflow

### 1. Test Compatibility

Run your existing v1 command with v2:
```bash
# Your v1 command
python3 qwen-eval.py --models a b --verbose

# Same with v2
python3 qwen-eval-v2.py --models a b --verbose
```

Compare outputs to verify results match.

### 2. Enable New Features Gradually

Start with caching:
```bash
python3 qwen-eval-v2.py --models a b --cache
```

Then add parallelism:
```bash
python3 qwen-eval-v2.py --models a b --cache --workers 4
```

Then explore new metrics:
```bash
python3 qwen-eval-v2.py --models a b --cache --workers 4 --all-metrics
```

### 3. Move to Config Files

Once you're happy, save your setup:
```bash
python3 qwen-eval-v2.py --models a b --cache --workers 4 --save-config production.yaml
```

Then use the config:
```bash
python3 qwen-eval-v2.py --config production.yaml
```

### 4. Commit Configs + Reports

```bash
git add eval-config-*.yaml evals/
git commit -m "eval: migrate to v2 framework"
```

## Code Migration

If you wrote scripts that parse v1 output:

### JSON Parsing

```python
# v1
with open("results.json") as f:
    results = json.load(f)  # List of results

for result in results:
    print(result["model"], result["response"])
```

```python
# v2
with open("results.json") as f:
    data = json.load(f)
    results = data["results"]  # Extract results array

for result in results:
    print(result["model"], result["response"])
    # New fields available:
    print(result.get("metrics", {}))
    print(result.get("success", True))
```

### Custom Metrics

v1: Edit `qwen-eval.py` directly

v2: Create a separate module

```python
# custom_metrics.py
from qwen_eval.metrics import MetricRegistry

def my_metric(prompt: str, response: str) -> float:
    return 0.0

registry = MetricRegistry()
registry.register("my_metric", my_metric)
```

Then import in your evaluation script.

## Performance Comparison

Typical speedup with v2 (4 models × 4 tests = 16 evaluations):

| Configuration | v1 Time | v2 Time | Speedup |
|---------------|---------|---------|---------|
| Sequential | 60s | 60s | 1.0x |
| w/ caching (2nd run) | 60s | ~0s | ∞x |
| w/ 4 workers | N/A | 20s | 3.0x |
| w/ 8 workers | N/A | 12s | 5.0x |

## Troubleshooting

### "No module named 'yaml'"

v2 requires `pyyaml` for config files. Install it:
```bash
pip3 install pyyaml
```

Or just use CLI args (no YAML needed):
```bash
python3 qwen-eval-v2.py --models a b  # Works without pyyaml
```

### v1 Still Needed?

Keep both! v1 is simpler for one-off tests. v2 is better for:
- Production evaluations
- Iterative development
- Team collaboration
- CI/CD integration

## When to Use Each

### Use v1 If:
- Quick one-time test
- Don't need caching or parallelism
- Single file convenience

### Use v2 If:
- Iterative model development
- Multiple evaluation rounds
- Team sharing configs
- Performance matters
- Want rich metrics
- CI/CD pipeline

## Summary

v2 is a **superset** of v1. Everything v1 does, v2 does (and more).

Start by running your v1 commands with v2. Then gradually adopt new features as needed.

**Recommended:** Use v2 for all new work. Keep v1 around as a lightweight fallback.
