"""Result reporters for different output formats."""

import json
import logging
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime
from collections import defaultdict

from .core import EvalResult

logger = logging.getLogger(__name__)


class BaseReporter:
    """Base class for result reporters."""
    
    def __init__(self, results: List[EvalResult]):
        self.results = results
        self.models = list(set(r.model for r in results))
        self.test_suites = list(set(r.test_suite for r in results))
    
    def generate(self) -> str:
        """Generate report content."""
        raise NotImplementedError
    
    def save(self, path: Path) -> None:
        """Save report to file."""
        content = self.generate()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        logger.info(f"Report saved to: {path}")


class JSONReporter(BaseReporter):
    """Export results as structured JSON."""
    
    def generate(self) -> str:
        """Generate JSON report."""
        
        report = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "total_results": len(self.results),
                "models": self.models,
                "test_suites": self.test_suites
            },
            "results": [r.to_dict() for r in self.results]
        }
        
        return json.dumps(report, indent=2)


class MarkdownReporter(BaseReporter):
    """Generate markdown evaluation reports."""
    
    def generate(self) -> str:
        """Generate markdown report."""
        
        lines = []
        
        # Header
        lines.extend(self._generate_header())
        
        # Summary statistics
        lines.extend(self._generate_summary())
        
        # Performance comparison
        lines.extend(self._generate_performance_table())
        
        # Metric comparison
        lines.extend(self._generate_metrics_comparison())
        
        # Detailed responses
        lines.extend(self._generate_detailed_responses())
        
        # Error summary if any
        failed = [r for r in self.results if not r.success]
        if failed:
            lines.extend(self._generate_error_summary(failed))
        
        return "\n".join(lines)
    
    def _generate_header(self) -> List[str]:
        """Generate report header."""
        return [
            "# Qwen Model Evaluation Report",
            "",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Models:** {', '.join(self.models)}",
            f"**Test Suites:** {', '.join(self.test_suites)}",
            f"**Total Evaluations:** {len(self.results)}",
            "",
            "---",
            ""
        ]
    
    def _generate_summary(self) -> List[str]:
        """Generate summary statistics."""
        lines = ["## Summary Statistics", ""]
        
        successful = [r for r in self.results if r.success]
        failed = [r for r in self.results if not r.success]
        
        lines.append(f"- **Successful:** {len(successful)}")
        lines.append(f"- **Failed:** {len(failed)}")
        
        if successful:
            avg_time = sum(r.total_time for r in successful) / len(successful)
            avg_speed = sum(r.tokens_per_sec for r in successful) / len(successful)
            
            lines.append(f"- **Average Time:** {avg_time:.2f}s")
            lines.append(f"- **Average Speed:** {avg_speed:.1f} tok/s")
        
        lines.append("")
        return lines
    
    def _generate_performance_table(self) -> List[str]:
        """Generate performance comparison table."""
        lines = ["## Performance Comparison", ""]
        
        lines.append("| Model | Avg Time (s) | Avg Speed (tok/s) | Success Rate |")
        lines.append("|-------|--------------|-------------------|--------------|")
        
        for model in self.models:
            model_results = [r for r in self.results if r.model == model]
            successful = [r for r in model_results if r.success]
            
            if not successful:
                lines.append(f"| {model} | N/A | N/A | 0% |")
                continue
            
            avg_time = sum(r.total_time for r in successful) / len(successful)
            avg_speed = sum(r.tokens_per_sec for r in successful) / len(successful)
            success_rate = (len(successful) / len(model_results)) * 100
            
            lines.append(
                f"| {model} | {avg_time:.2f} | {avg_speed:.1f} | {success_rate:.0f}% |"
            )
        
        lines.append("")
        return lines
    
    def _generate_metrics_comparison(self) -> List[str]:
        """Generate metrics comparison section."""
        lines = ["## Metrics Comparison", ""]
        
        # Gather all metric names
        all_metrics = set()
        for r in self.results:
            if r.success and r.metrics:
                all_metrics.update(r.metrics.keys())
        
        if not all_metrics:
            lines.append("*No metrics computed*")
            lines.append("")
            return lines
        
        # Group by test
        test_names = list(set(r.test_name for r in self.results))
        
        for test_name in sorted(test_names):
            lines.append(f"### Test: {test_name}")
            lines.append("")
            
            test_results = [r for r in self.results if r.test_name == test_name and r.success]
            
            if not test_results:
                lines.append("*No successful results*")
                lines.append("")
                continue
            
            # Create metric table
            lines.append("| Model | " + " | ".join(sorted(all_metrics)) + " |")
            lines.append("|-------|" + "|".join(["---"] * len(all_metrics)) + "|")
            
            for model in self.models:
                model_result = next((r for r in test_results if r.model == model), None)
                
                if not model_result:
                    continue
                
                metric_values = []
                for metric in sorted(all_metrics):
                    value = model_result.metrics.get(metric, "N/A")
                    if isinstance(value, dict):
                        # Handle dict metrics (like personal_pronouns)
                        value = f"{value.get('total', 'N/A')}"
                    elif isinstance(value, float):
                        value = f"{value:.2f}"
                    metric_values.append(str(value))
                
                lines.append(f"| {model} | " + " | ".join(metric_values) + " |")
            
            lines.append("")
        
        return lines
    
    def _generate_detailed_responses(self) -> List[str]:
        """Generate detailed response comparisons."""
        lines = ["## Detailed Responses", ""]
        
        # Group by prompt
        prompts = list(set(r.prompt for r in self.results))
        
        for prompt in prompts:
            lines.append(f"### Prompt: {prompt}")
            lines.append("")
            
            for model in self.models:
                result = next(
                    (r for r in self.results if r.model == model and r.prompt == prompt),
                    None
                )
                
                if not result:
                    continue
                
                lines.append(f"#### {model}")
                
                if result.success:
                    lines.append(
                        f"*Time: {result.total_time:.2f}s | "
                        f"Speed: {result.tokens_per_sec:.1f} tok/s*"
                    )
                    lines.append("")
                    lines.append(result.response)
                else:
                    lines.append(f"**ERROR:** {result.error}")
                
                lines.append("")
        
        return lines
    
    def _generate_error_summary(self, failed: List[EvalResult]) -> List[str]:
        """Generate error summary."""
        lines = ["## Errors", ""]
        
        # Group errors by type
        error_groups = defaultdict(list)
        for r in failed:
            error_groups[r.error].append(f"{r.model}/{r.test_name}")
        
        for error, instances in error_groups.items():
            lines.append(f"### {error}")
            lines.append("")
            for instance in instances:
                lines.append(f"- {instance}")
            lines.append("")
        
        return lines


class ComparisonReporter(BaseReporter):
    """Generate side-by-side comparison reports."""
    
    def generate(self) -> str:
        """Generate comparison report."""
        lines = []
        
        lines.append("# Model Comparison Report")
        lines.append("")
        lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("")
        
        # Get all unique prompts
        prompts = list(set(r.prompt for r in self.results))
        
        for prompt in prompts:
            lines.append("=" * 80)
            lines.append(f"PROMPT: {prompt}")
            lines.append("=" * 80)
            lines.append("")
            
            for model in self.models:
                result = next(
                    (r for r in self.results if r.model == model and r.prompt == prompt),
                    None
                )
                
                if not result:
                    continue
                
                lines.append(f"[{model}]")
                
                if result.success:
                    lines.append(
                        f"Time: {result.total_time:.2f}s | "
                        f"Speed: {result.tokens_per_sec:.1f} tok/s"
                    )
                    lines.append("-" * 80)
                    lines.append(result.response)
                else:
                    lines.append(f"ERROR: {result.error}")
                
                lines.append("")
        
        return "\n".join(lines)
