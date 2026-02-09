# Model Evaluation Framework

Sophisticated toolkit for evaluating Qwen model variants and LoRA fine-tuned models.

## Quick Start

```bash
# Install dependencies
pip3 install -r requirements-eval.txt

# List test suites
python3 qwen-eval-v2.py --list-suites

# Run evaluation
python3 qwen-eval-v2.py --models qwen2.5:8b qwen-8b-dialog-v1 --verbose
```

## Documentation

- **[QWEN-EVAL-V2-README.md](QWEN-EVAL-V2-README.md)** - Comprehensive guide (v2 framework)
- **[MIGRATION-V1-TO-V2.md](MIGRATION-V1-TO-V2.md)** - Migration guide from v1
- **[QWEN-EVAL-README.md](QWEN-EVAL-README.md)** - v1 documentation

## Structure

```
evaluation/
├── README.md                   # This file
├── qwen-eval-v2.py            # Main CLI (v2 - recommended)
├── qwen-eval.py               # Legacy CLI (v1 - simple)
├── qwen_eval/                 # Core package
│   ├── config.py              # Configuration & logging
│   ├── core.py                # Evaluation engine
│   ├── test_suites.py         # Built-in test suites
│   ├── metrics.py             # Metric registry (15+ metrics)
│   └── reporters.py           # Output formatters
├── eval-config-example.yaml   # Example configuration
├── requirements-eval.txt      # Python dependencies
├── QWEN-EVAL-V2-README.md    # Full documentation
└── MIGRATION-V1-TO-V2.md     # Upgrade guide
```

## Features

- **Parallel execution** - Run evaluations concurrently
- **Result caching** - Avoid redundant inference
- **YAML configs** - Reproducible evaluations
- **15+ metrics** - Pedagogical quality, dialogue, complexity
- **4 test suites** - Pedagogical, dialogue, baseline, stress
- **3 reporters** - JSON, Markdown, side-by-side comparison
- **Extensible** - Add custom metrics and test suites

## Workflow

### 1. Basic Evaluation
```bash
python3 qwen-eval-v2.py --models base-model fine-tuned-v1
```

### 2. With Config File
```bash
python3 qwen-eval-v2.py --config eval-config-example.yaml
```

### 3. Parallel + Cached
```bash
python3 qwen-eval-v2.py --workers 8 --cache --verbose
```

## See Also

- Main project: [../README.md](../README.md)
- Fine-tuning workflows: [../fine-tuning/](../fine-tuning/)
- Training logs: [../DEVLOG.md](../DEVLOG.md)
