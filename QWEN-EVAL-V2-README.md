

# Qwen Model Evaluation Framework v2

**Sophisticated, maintainable evaluation toolkit for LLM variants**

## What's New in v2

### Architecture Improvements
- ✅ **Modular design**: Clean separation of concerns (core, metrics, reporters, config)
- ✅ **Type hints**: Full type coverage for better IDE support and maintainability
- ✅ **Logging**: Proper logging framework (replaces print statements)
- ✅ **Error handling**: Robust exception handling and recovery
- ✅ **Caching**: Intelligent result caching to avoid re-running evaluations

### Features
- ⚡ **Parallel execution**: Run multiple models concurrently (configurable workers)
- 📊 **Rich metrics**: 15+ built-in metrics for pedagogical quality, dialogue, and complexity
- 📝 **Multiple reporters**: JSON, Markdown, and side-by-side comparison formats
- ⚙️ **Configuration files**: YAML-based config for reproducible evaluations
- 🧪 **Custom test suites**: Easy to define domain-specific tests
- 🔌 **Plugin system**: Extensible metric registry

## Quick Start

### Installation

```bash
# Install dependencies
pip3 install -r requirements-eval.txt

# Verify setup
python3 qwen-eval-v2.py --list-suites
```

### Basic Usage

```bash
# Run evaluation with defaults
python3 qwen-eval-v2.py

# Evaluate specific models
python3 qwen-eval-v2.py --models qwen2.5:8b qwen-8b-dialog-v1 custom-model

# Use different test suite
python3 qwen-eval-v2.py --test-suite dialogue --verbose

# Enable parallel execution + caching
python3 qwen-eval-v2.py --workers 8 --cache
```

## Architecture

```
qwen_eval/
├── __init__.py           # Package exports
├── config.py             # Configuration management
├── core.py               # Evaluation engine
├── test_suites.py        # Built-in and custom test suites
├── metrics.py            # Metric registry and implementations
└── reporters.py          # Result formatting and export

qwen-eval-v2.py           # Main CLI entry point
```

### Design Principles

1. **Separation of Concerns**: Each module has a single, well-defined responsibility
2. **Extensibility**: Easy to add custom metrics, test suites, and reporters
3. **Robustness**: Graceful error handling, caching, and recovery
4. **Performance**: Parallel execution, intelligent caching
5. **Usability**: Clean CLI, YAML configs, detailed logging

## Configuration

### CLI Arguments

```bash
python3 qwen-eval-v2.py --help
```

Key options:
- `--models`: Models to evaluate
- `--test-suite`: Test suite (name or YAML path)
- `--workers`: Parallel workers (default: 4)
- `--cache`: Enable result caching
- `--metrics`: Metrics to compute
- `--output`: JSON output path
- `--report`: Markdown report path
- `--verbose`: Detailed progress logging

### YAML Configuration

Create a config file for reproducible evaluations:

```yaml
# my-eval.yaml
models:
  - qwen2.5:8b
  - qwen-8b-dialog-v1
  - qwen-8b-dialog-v2

test_suite: pedagogical

output_dir: ./evals
output_json: results.json
output_report: report.md

timeout: 60
max_workers: 8
cache_results: true

include_metrics:
  - question_count
  - question_ratio
  - inquiry_markers
  - collaborative_markers
  - lexical_diversity

verbose: true
log_level: INFO
```

Run with config:
```bash
python3 qwen-eval-v2.py --config my-eval.yaml
```

Save CLI args as config:
```bash
python3 qwen-eval-v2.py --models a b c --save-config saved.yaml
```

## Test Suites

### Built-in Suites

#### 1. **Pedagogical** (default)
Tests for inquiry-led, scaffolding dialogue:
- `scaffolding_inquiry`: Avoid direct answers, scaffold thinking
- `adaptive_depth`: Probe understanding before explaining
- `socratic_method`: Guide through questions vs showing steps
- `metacognitive`: Help identify existing knowledge
- `conceptual_confusion`: Explore confusion, ask diagnostic questions

**Use case:** Evaluating tutoring and teaching capabilities

#### 2. **Dialogue**
Multi-turn conversational patterns:
- `multi_turn_context`: Establish context through questions
- `collaborative`: Invite co-investigation
- `open_ended`: Guide discovery, explore interests

**Use case:** Conversational flow and engagement

#### 3. **Baseline**
Sanity checks for basic functionality:
- `factual_recall`: Simple facts
- `basic_instruction`: Technical explanations
- `math_problem`: Numerical accuracy

**Use case:** Regression testing, ensuring models aren't broken

#### 4. **Stress**
Edge cases and challenging scenarios:
- `ambiguous_question`: Handle ambiguity, clarify intent
- `multiple_concepts`: Manage complexity
- `misconception`: Gently correct errors

**Use case:** Robustness testing

### Custom Test Suites

Export a template:
```bash
python3 qwen-eval-v2.py --export-template my-tests.yaml
```

Edit the YAML:
```yaml
name: esl_tutoring
description: ESL-specific dialogue tests

tests:
  - name: grammar_scaffolding
    prompt: "I always confuse 'their' and 'there'. Can you help?"
    criteria: "Should probe understanding, not just give rules"
    tags: [grammar, esl]
  
  - name: pronunciation_inquiry
    prompt: "How do I pronounce 'colonel'?"
    criteria: "Should ask about context, prior attempts"
    tags: [pronunciation, esl]
```

Run it:
```bash
python3 qwen-eval-v2.py --test-suite my-tests.yaml
```

## Metrics

### Built-in Metrics

#### Basic
- `response_length`: Character count
- `word_count`: Total words
- `sentence_count`: Number of sentences

#### Pedagogical
- `question_count`: Number of questions
- `question_ratio`: Questions per sentence
- `imperative_count`: Command-style sentences ("Consider...", "Try...")
- `inquiry_markers`: "What do you think", "Can you tell me"

#### Dialogue
- `collaborative_markers`: "Let's", "We can", "Together"
- `personal_pronouns`: First/second person usage
- `hedging_phrases`: Uncertainty markers ("might", "perhaps")

#### Complexity
- `avg_sentence_length`: Words per sentence
- `unique_words`: Vocabulary count
- `lexical_diversity`: Type-token ratio

### Custom Metrics

Add your own metrics by extending the registry:

```python
# custom_metrics.py
from qwen_eval.metrics import MetricRegistry

def pedagogical_score(prompt: str, response: str) -> float:
    """
    Custom scoring combining multiple factors.
    Returns 0.0 - 1.0
    """
    questions = response.count('?')
    imperatives = len(re.findall(r'\b(Consider|Think|Try)\b', response))
    
    # Your scoring logic here
    score = (questions * 0.5 + imperatives * 0.3) / 10
    return min(score, 1.0)

# Register it
registry = MetricRegistry()
registry.register("pedagogical_score", pedagogical_score)
```

Then include it:
```bash
python3 qwen-eval-v2.py --metrics pedagogical_score
```

## Reporters

### JSON Reporter
Structured data for programmatic analysis:
```json
{
  "metadata": {
    "generated_at": "2026-02-08T21:30:00",
    "total_results": 24,
    "models": ["qwen2.5:8b", "qwen-8b-dialog-v1"]
  },
  "results": [...]
}
```

### Markdown Reporter
Human-readable evaluation report:
- Summary statistics
- Performance comparison table
- Metrics comparison per test
- Detailed response comparisons
- Error summary

### Comparison Reporter
Side-by-side text format for easy diffing:
```
========================================
PROMPT: I'm struggling to understand...
========================================

[qwen2.5:8b]
Time: 3.2s | Speed: 42.3 tok/s
----------------------------------------
[response here]

[qwen-8b-dialog-v1]
Time: 3.5s | Speed: 38.1 tok/s
----------------------------------------
[response here]
```

## Workflow Examples

### Stage 1: Baseline Evaluation

Establish baseline performance:

```bash
python3 qwen-eval-v2.py \
  --models qwen2.5:8b qwen-8b-dialog-v1 \
  --test-suite pedagogical \
  --workers 8 \
  --cache \
  --output baseline-results.json \
  --report baseline-report.md \
  --comparison baseline-compare.txt \
  --verbose
```

### Stage 2: LoRA Iteration

Compare new variant against current best:

```bash
python3 qwen-eval-v2.py \
  --models qwen-8b-dialog-v1 qwen-8b-dialog-v2 \
  --test-suite pedagogical \
  --cache \
  --output v2-vs-v1.json \
  --report v2-vs-v1.md
```

### Stage 3: Regression Testing

Full test suite before production:

```bash
# Run all test suites
for suite in pedagogical dialogue baseline stress; do
  python3 qwen-eval-v2.py \
    --models qwen-8b-NEW \
    --test-suite $suite \
    --cache \
    --output "regression-${suite}.json" \
    --report "regression-${suite}.md"
done
```

### Stage 4: Automated Evaluation

Create a config for CI/CD:

```yaml
# ci-eval.yaml
models:
  - qwen-8b-production
  - qwen-8b-candidate

test_suite: baseline
cache_results: true
max_workers: 16

output_dir: ./ci-evals
output_json: ci-results.json
output_report: ci-report.md

log_level: WARNING
```

Run in CI:
```bash
python3 qwen-eval-v2.py --config ci-eval.yaml
```

## Performance & Caching

### Parallel Execution

Use `--workers` to control parallelism:
```bash
# Fast: 8 parallel workers
python3 qwen-eval-v2.py --workers 8

# Conservative: 2 workers (if system under load)
python3 qwen-eval-v2.py --workers 2
```

**Rule of thumb:** `workers = CPU cores - 1` for best performance

### Result Caching

Enable caching to avoid re-running evaluations:
```bash
python3 qwen-eval-v2.py --cache
```

Cache is keyed by: `(model, prompt, test_suite)`

**When to clear cache:**
- Model updated but name unchanged
- Test suite definition changed
- After investigating anomalies

```bash
python3 qwen-eval-v2.py --clear-cache --cache
```

Cache location: `{output_dir}/.cache/`

## Logging

Control verbosity:
```bash
# Quiet (errors only)
python3 qwen-eval-v2.py --quiet

# Normal (warnings + errors)
python3 qwen-eval-v2.py

# Verbose (info + warnings + errors)
python3 qwen-eval-v2.py --verbose

# Debug (everything)
python3 qwen-eval-v2.py --debug
```

Logs include:
- Evaluation progress
- Cache hits/misses
- Performance metrics
- Error details with stack traces

## Extending the Framework

### Adding a New Metric

1. Define the metric function:
```python
# qwen_eval/metrics.py

def my_custom_metric(prompt: str, response: str) -> float:
    """Your metric logic here."""
    return 0.0
```

2. Register it:
```python
# In MetricRegistry._register_default_metrics()
self.register("my_custom_metric", my_custom_metric)
```

3. Use it:
```bash
python3 qwen-eval-v2.py --metrics my_custom_metric
```

### Adding a New Reporter

1. Subclass `BaseReporter`:
```python
# qwen_eval/reporters.py

class CSVReporter(BaseReporter):
    def generate(self) -> str:
        """Generate CSV output."""
        # Your CSV generation logic
        return csv_content
```

2. Use it in CLI:
```python
# qwen-eval-v2.py
reporter = CSVReporter(results)
reporter.save(args.csv_output)
```

### Adding a New Test Suite

Just create a YAML file:
```yaml
name: my_domain
description: Domain-specific tests

tests:
  - name: test1
    prompt: "..."
    criteria: "..."
    tags: [domain, specific]
```

## Comparison: v1 vs v2

| Feature | v1 | v2 |
|---------|----|----|
| **Architecture** | Single file | Modular package |
| **Parallelism** | No | Yes (configurable workers) |
| **Caching** | No | Yes (file-based cache) |
| **Config Files** | No | Yes (YAML) |
| **Logging** | print() | logging framework |
| **Metrics** | 3 basic | 15+ extensible |
| **Reporters** | 2 | 3 (+ extensible) |
| **Error Handling** | Basic | Robust with recovery |
| **Type Hints** | Minimal | Full coverage |
| **Custom Tests** | Code edit | YAML files |

## Best Practices

### Reproducibility
- Use YAML configs for important evaluations
- Commit configs + reports to git
- Tag releases alongside model checkpoints

### Performance
- Enable caching for iterative development
- Use parallel workers on multi-core systems
- Clear cache when model/tests change

### Iteration
- Start with `baseline` suite (fast sanity check)
- Move to `pedagogical` for quality assessment
- Run `stress` before production deployment

### Comparison
- Always include base model as reference
- Use `--comparison` for side-by-side review
- Track metrics over time (commit JSON results)

### Organization
```
evals/
├── configs/
│   ├── baseline.yaml
│   ├── pedagogical.yaml
│   └── regression.yaml
├── results/
│   ├── 20260208-baseline.json
│   └── 20260208-pedagogical.json
├── reports/
│   ├── 20260208-baseline.md
│   └── 20260208-pedagogical.md
└── .cache/
    └── [cached results]
```

## Troubleshooting

### "Ollama command not found"
```bash
# Check if ollama is installed
which ollama

# Install if needed (macOS)
brew install ollama
```

### Timeout Errors
Increase timeout for large models:
```bash
python3 qwen-eval-v2.py --timeout 120
```

### Out of Memory
Reduce parallel workers:
```bash
python3 qwen-eval-v2.py --workers 2
```

### Cache Issues
Clear and rebuild:
```bash
python3 qwen-eval-v2.py --clear-cache --cache
```

## Roadmap

Planned improvements:
- [ ] GPT-4 as judge (automated quality scoring)
- [ ] Multi-turn conversation evaluation
- [ ] Visualization (charts, heatmaps)
- [ ] Statistical significance testing
- [ ] Export to wandb/mlflow
- [ ] Human evaluation interface
- [ ] Batch processing from directories

## Contributing

Found a bug? Want a feature? Open an issue or PR!

### Development Setup
```bash
# Install dev dependencies
pip3 install -r requirements-eval.txt

# Run tests (when added)
python3 -m pytest tests/

# Format code
black qwen_eval/ qwen-eval-v2.py
```

## License

MIT (or your license here)

## References

- Base model: [Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B)
- Dialog-v1: [milwright/qwen-8b-dialog-v1](https://huggingface.co/milwright/qwen-8b-dialog-v1)
- Magpie dataset: [Magpie-Align/Magpie-Pro-300K-Filtered](https://huggingface.co/datasets/Magpie-Align/Magpie-Pro-300K-Filtered)

---

**Built with care for maintainability and sophistication** 🜁
