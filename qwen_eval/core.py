"""Core evaluation engine."""

import subprocess
import time
import logging
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
import hashlib
import json

from .config import EvalConfig
from .test_suites import TestSuite, load_test_suite
from .metrics import MetricRegistry

logger = logging.getLogger(__name__)


@dataclass
class EvalResult:
    """Single evaluation result with rich metadata."""
    
    model: str
    prompt: str
    response: str
    
    # Performance
    total_time: float
    tokens_per_sec: float
    
    # Metadata
    timestamp: str
    test_name: str
    test_suite: str
    
    # Metrics
    metrics: Dict[str, Any] = field(default_factory=dict)
    
    # Error tracking
    error: Optional[str] = None
    
    @property
    def success(self) -> bool:
        """Check if evaluation succeeded."""
        return self.error is None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "model": self.model,
            "prompt": self.prompt,
            "response": self.response,
            "total_time": self.total_time,
            "tokens_per_sec": self.tokens_per_sec,
            "timestamp": self.timestamp,
            "test_name": self.test_name,
            "test_suite": self.test_suite,
            "metrics": self.metrics,
            "error": self.error,
            "success": self.success
        }
    
    def cache_key(self) -> str:
        """Generate cache key for this result."""
        key_str = f"{self.model}:{self.prompt}:{self.test_suite}"
        return hashlib.md5(key_str.encode()).hexdigest()


class ResultCache:
    """Simple file-based result cache."""
    
    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Cache directory: {self.cache_dir}")
    
    def get(self, cache_key: str) -> Optional[Dict[str, Any]]:
        """Retrieve cached result."""
        cache_file = self.cache_dir / f"{cache_key}.json"
        
        if not cache_file.exists():
            return None
        
        try:
            with open(cache_file) as f:
                result = json.load(f)
            logger.debug(f"Cache hit: {cache_key}")
            return result
        except Exception as e:
            logger.warning(f"Cache read error for {cache_key}: {e}")
            return None
    
    def set(self, cache_key: str, result: Dict[str, Any]) -> None:
        """Store result in cache."""
        cache_file = self.cache_dir / f"{cache_key}.json"
        
        try:
            with open(cache_file, 'w') as f:
                json.dump(result, f, indent=2)
            logger.debug(f"Cached result: {cache_key}")
        except Exception as e:
            logger.warning(f"Cache write error for {cache_key}: {e}")
    
    def clear(self) -> None:
        """Clear all cached results."""
        for cache_file in self.cache_dir.glob("*.json"):
            cache_file.unlink()
        logger.info("Cache cleared")


class OllamaRunner:
    """Handle Ollama model inference."""
    
    def __init__(self, timeout: int = 60):
        self.timeout = timeout
    
    def run(self, model: str, prompt: str) -> Dict[str, Any]:
        """
        Run inference with error handling and timing.
        
        Returns:
            dict with 'response', 'time', 'tokens_per_sec', 'error'
        """
        start = time.time()
        
        try:
            result = subprocess.run(
                ["ollama", "run", model, prompt],
                capture_output=True,
                text=True,
                timeout=self.timeout
            )
            
            elapsed = time.time() - start
            
            if result.returncode != 0:
                logger.error(f"Ollama error for {model}: {result.stderr}")
                return {
                    "response": "",
                    "time": elapsed,
                    "tokens_per_sec": 0,
                    "error": result.stderr.strip()
                }
            
            response = result.stdout.strip()
            
            # Token estimation (rough)
            estimated_tokens = len(response.split()) * 1.3
            tokens_per_sec = estimated_tokens / elapsed if elapsed > 0 else 0
            
            logger.info(f"{model}: {elapsed:.2f}s, {tokens_per_sec:.1f} tok/s")
            
            return {
                "response": response,
                "time": elapsed,
                "tokens_per_sec": tokens_per_sec,
                "error": None
            }
            
        except subprocess.TimeoutExpired:
            logger.warning(f"Timeout ({self.timeout}s) for {model}")
            return {
                "response": "",
                "time": self.timeout,
                "tokens_per_sec": 0,
                "error": f"Timeout after {self.timeout}s"
            }
        except FileNotFoundError:
            logger.error("Ollama not found - is it installed?")
            return {
                "response": "",
                "time": 0,
                "tokens_per_sec": 0,
                "error": "Ollama command not found"
            }
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            return {
                "response": "",
                "time": 0,
                "tokens_per_sec": 0,
                "error": str(e)
            }


class ModelEvaluator:
    """Main evaluation orchestrator."""
    
    def __init__(self, config: EvalConfig):
        self.config = config
        self.runner = OllamaRunner(timeout=config.timeout)
        self.metrics = MetricRegistry()
        
        # Setup cache
        if config.cache_results:
            cache_dir = config.output_dir / ".cache"
            self.cache = ResultCache(cache_dir)
        else:
            self.cache = None
        
        logger.info(f"Evaluator initialized: {len(config.models)} models")
    
    def evaluate_single(
        self,
        model: str,
        test: Dict[str, str],
        test_suite_name: str
    ) -> EvalResult:
        """Evaluate a single model on a single test."""
        
        # Check cache first
        cache_key = hashlib.md5(
            f"{model}:{test['prompt']}:{test_suite_name}".encode()
        ).hexdigest()
        
        if self.cache:
            cached = self.cache.get(cache_key)
            if cached:
                logger.debug(f"Using cached result for {model}/{test['name']}")
                return EvalResult(**cached)
        
        # Run inference
        logger.info(f"Evaluating {model} on {test['name']}")
        inference = self.runner.run(model, test['prompt'])
        
        # Compute metrics
        computed_metrics = {}
        if inference['error'] is None:
            for metric_name in self.config.include_metrics:
                try:
                    metric_fn = self.metrics.get(metric_name)
                    computed_metrics[metric_name] = metric_fn(
                        prompt=test['prompt'],
                        response=inference['response']
                    )
                except Exception as e:
                    logger.warning(f"Metric {metric_name} failed: {e}")
                    computed_metrics[metric_name] = None
        
        # Create result
        result = EvalResult(
            model=model,
            prompt=test['prompt'],
            response=inference['response'],
            total_time=inference['time'],
            tokens_per_sec=inference['tokens_per_sec'],
            timestamp=datetime.now().isoformat(),
            test_name=test['name'],
            test_suite=test_suite_name,
            metrics=computed_metrics,
            error=inference['error']
        )
        
        # Cache if enabled
        if self.cache:
            self.cache.set(cache_key, result.to_dict())
        
        return result
    
    def evaluate_parallel(
        self,
        models: List[str],
        test_suite: TestSuite
    ) -> List[EvalResult]:
        """Evaluate multiple models in parallel."""
        
        results = []
        
        # Create all tasks
        tasks = []
        for model in models:
            for test in test_suite.tests:
                tasks.append((model, test, test_suite.name))
        
        logger.info(f"Running {len(tasks)} evaluations with {self.config.max_workers} workers")
        
        # Execute in parallel
        with ThreadPoolExecutor(max_workers=self.config.max_workers) as executor:
            future_to_task = {
                executor.submit(self.evaluate_single, model, test, suite_name): (model, test['name'])
                for model, test, suite_name in tasks
            }
            
            for future in as_completed(future_to_task):
                model, test_name = future_to_task[future]
                try:
                    result = future.result()
                    results.append(result)
                    
                    if self.config.verbose:
                        status = "✓" if result.success else "✗"
                        print(f"  {status} {model}/{test_name}: {result.total_time:.2f}s")
                        
                except Exception as e:
                    logger.error(f"Task failed for {model}/{test_name}: {e}", exc_info=True)
        
        return results
    
    def evaluate(self) -> List[EvalResult]:
        """Run full evaluation suite."""
        
        # Load test suite
        test_suite = load_test_suite(self.config.test_suite)
        logger.info(f"Test suite: {test_suite.name} ({len(test_suite.tests)} tests)")
        
        # Run evaluations
        if self.config.max_workers > 1:
            results = self.evaluate_parallel(self.config.models, test_suite)
        else:
            # Sequential fallback
            results = []
            for model in self.config.models:
                for test in test_suite.tests:
                    result = self.evaluate_single(model, test, test_suite.name)
                    results.append(result)
        
        logger.info(f"Evaluation complete: {len(results)} results")
        
        # Filter out errors if needed
        successful = [r for r in results if r.success]
        failed = [r for r in results if not r.success]
        
        if failed:
            logger.warning(f"{len(failed)} evaluations failed")
            for r in failed:
                logger.warning(f"  {r.model}/{r.test_name}: {r.error}")
        
        return results
