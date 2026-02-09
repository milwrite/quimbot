#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qwen Model Evaluation Framework v2
Sophisticated evaluation toolkit for LLM variants.

Usage:
    qwen-eval-v2.py --models qwen2.5:8b qwen-8b-dialog-v1
    qwen-eval-v2.py --config eval-config.yaml
    qwen-eval-v2.py --list-suites
    qwen-eval-v2.py --export-template my-tests.yaml
"""

import sys
import argparse
import logging
from pathlib import Path

# Add qwen_eval to path
sys.path.insert(0, str(Path(__file__).parent))

from qwen_eval import ModelEvaluator, EvalConfig
from qwen_eval.config import setup_logging
from qwen_eval.test_suites import list_test_suites, export_test_suite_template
from qwen_eval.reporters import MarkdownReporter, JSONReporter, ComparisonReporter

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate Qwen model variants with sophisticated metrics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic evaluation
  %(prog)s --models qwen2.5:8b qwen-8b-dialog-v1
  
  # Load from config file
  %(prog)s --config my-eval.yaml
  
  # Custom test suite
  %(prog)s --test-suite custom-tests.yaml --verbose
  
  # Parallel execution
  %(prog)s --workers 8 --cache
  
  # Export results
  %(prog)s --output results.json --report report.md --comparison compare.txt
        """
    )
    
    # Configuration
    config_group = parser.add_argument_group("configuration")
    config_group.add_argument(
        "--config",
        type=Path,
        help="Load configuration from YAML file"
    )
    config_group.add_argument(
        "--save-config",
        type=Path,
        help="Save current configuration to YAML file"
    )
    
    # Model selection
    model_group = parser.add_argument_group("models")
    model_group.add_argument(
        "--models",
        nargs="+",
        default=["qwen2.5:8b", "qwen-8b-dialog-v1"],
        help="Models to evaluate (default: base + dialog-v1)"
    )
    
    # Test suite
    suite_group = parser.add_argument_group("test suite")
    suite_group.add_argument(
        "--test-suite",
        default="pedagogical",
        help="Test suite name or path to YAML file (default: pedagogical)"
    )
    suite_group.add_argument(
        "--list-suites",
        action="store_true",
        help="List available built-in test suites"
    )
    suite_group.add_argument(
        "--export-template",
        type=Path,
        metavar="PATH",
        help="Export a test suite YAML template"
    )
    
    # Output
    output_group = parser.add_argument_group("output")
    output_group.add_argument(
        "--output",
        type=Path,
        help="Save results as JSON"
    )
    output_group.add_argument(
        "--report",
        type=Path,
        help="Save detailed markdown report"
    )
    output_group.add_argument(
        "--comparison",
        type=Path,
        help="Save side-by-side comparison report"
    )
    output_group.add_argument(
        "--output-dir",
        type=Path,
        default=Path("./evals"),
        help="Output directory (default: ./evals)"
    )
    
    # Performance
    perf_group = parser.add_argument_group("performance")
    perf_group.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Number of parallel workers (default: 4)"
    )
    perf_group.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="Inference timeout in seconds (default: 60)"
    )
    perf_group.add_argument(
        "--cache",
        action="store_true",
        help="Enable result caching"
    )
    perf_group.add_argument(
        "--clear-cache",
        action="store_true",
        help="Clear cache before running"
    )
    
    # Metrics
    metric_group = parser.add_argument_group("metrics")
    metric_group.add_argument(
        "--metrics",
        nargs="+",
        default=["response_length", "question_count", "question_ratio", "inquiry_markers"],
        help="Metrics to compute (default: basic set)"
    )
    metric_group.add_argument(
        "--all-metrics",
        action="store_true",
        help="Compute all available metrics"
    )
    
    # Logging
    log_group = parser.add_argument_group("logging")
    log_group.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    log_group.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging"
    )
    log_group.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress all output except errors"
    )
    
    args = parser.parse_args()
    
    # Setup logging
    if args.quiet:
        log_level = "ERROR"
    elif args.debug:
        log_level = "DEBUG"
    elif args.verbose:
        log_level = "INFO"
    else:
        log_level = "WARNING"
    
    setup_logging(log_level)
    
    # Handle utility commands
    if args.list_suites:
        print("\nAvailable built-in test suites:")
        for name, suite in list_test_suites().items():
            print(f"\n{name}:")
            print(f"  {suite.description}")
            print(f"  Tests: {len(suite.tests)}")
            for test in suite.tests:
                tags = test.get('tags', [])
                tag_str = f" [{', '.join(tags)}]" if tags else ""
                print(f"    - {test['name']}{tag_str}")
        return 0
    
    if args.export_template:
        export_test_suite_template(args.export_template)
        print(f"✓ Template exported to: {args.export_template}")
        return 0
    
    # Load or create config
    if args.config:
        config = EvalConfig.from_yaml(args.config)
        logger.info(f"Loaded config from: {args.config}")
    else:
        # Build config from CLI args
        metrics = args.metrics
        if args.all_metrics:
            from qwen_eval.metrics import MetricRegistry
            registry = MetricRegistry()
            metrics = registry.list()
        
        config = EvalConfig(
            models=args.models,
            test_suite=args.test_suite,
            output_json=args.output,
            output_report=args.report,
            output_dir=args.output_dir,
            timeout=args.timeout,
            max_workers=args.workers,
            cache_results=args.cache,
            verbose=args.verbose,
            log_level=log_level,
            include_metrics=metrics
        )
    
    # Save config if requested
    if args.save_config:
        config.to_yaml(args.save_config)
        logger.info(f"Config saved to: {args.save_config}")
    
    # Clear cache if requested
    if args.clear_cache and config.cache_results:
        from qwen_eval.core import ResultCache
        cache = ResultCache(config.output_dir / ".cache")
        cache.clear()
        print("✓ Cache cleared")
    
    # Run evaluation
    print(f"\n🔬 Qwen Model Evaluation v2")
    print(f"Models: {', '.join(config.models)}")
    print(f"Test Suite: {config.test_suite}")
    print(f"Workers: {config.max_workers}")
    print(f"Cache: {'enabled' if config.cache_results else 'disabled'}")
    print(f"Metrics: {', '.join(config.include_metrics[:3])}{'...' if len(config.include_metrics) > 3 else ''}")
    print("")
    
    try:
        evaluator = ModelEvaluator(config)
        results = evaluator.evaluate()
        
        print(f"\n✅ Evaluation complete: {len(results)} results")
        
        # Generate reports
        if config.output_json:
            reporter = JSONReporter(results)
            reporter.save(config.output_json)
            print(f"✓ JSON saved: {config.output_json}")
        
        if config.output_report:
            reporter = MarkdownReporter(results)
            reporter.save(config.output_report)
            print(f"✓ Report saved: {config.output_report}")
        
        if args.comparison:
            reporter = ComparisonReporter(results)
            reporter.save(args.comparison)
            print(f"✓ Comparison saved: {args.comparison}")
        
        # Default outputs if nothing specified
        if not (config.output_json or config.output_report or args.comparison):
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            
            json_path = config.output_dir / f"results-{timestamp}.json"
            reporter = JSONReporter(results)
            reporter.save(json_path)
            print(f"✓ JSON saved: {json_path}")
            
            report_path = config.output_dir / f"report-{timestamp}.md"
            reporter = MarkdownReporter(results)
            reporter.save(report_path)
            print(f"✓ Report saved: {report_path}")
        
        # Summary statistics
        successful = [r for r in results if r.success]
        failed = [r for r in results if not r.success]
        
        print(f"\n📊 Summary:")
        print(f"  Success: {len(successful)}/{len(results)}")
        if failed:
            print(f"  Failed: {len(failed)}")
        
        if successful:
            avg_time = sum(r.total_time for r in successful) / len(successful)
            avg_speed = sum(r.tokens_per_sec for r in successful) / len(successful)
            print(f"  Avg Time: {avg_time:.2f}s")
            print(f"  Avg Speed: {avg_speed:.1f} tok/s")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        return 130
    except Exception as e:
        logger.error(f"Evaluation failed: {e}", exc_info=True)
        print(f"\n❌ Error: {e}")
        return 1


if __name__ == "__main__":
    from datetime import datetime
    sys.exit(main())
