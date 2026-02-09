"""Configuration management for evaluation framework."""

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


@dataclass
class EvalConfig:
    """Evaluation configuration with validation."""
    
    models: List[str] = field(default_factory=lambda: ["qwen2.5:8b", "qwen-8b-dialog-v1"])
    test_suite: str = "pedagogical"
    output_json: Optional[Path] = None
    output_report: Optional[Path] = None
    output_dir: Path = Path("./evals")
    
    # Performance settings
    timeout: int = 60
    max_workers: int = 4
    cache_results: bool = True
    
    # Reporting
    verbose: bool = False
    log_level: str = "INFO"
    include_metrics: List[str] = field(default_factory=lambda: [
        "response_length",
        "question_count",
        "tokens_per_sec"
    ])
    
    # Advanced
    custom_prompts: Optional[Path] = None
    temperature: float = 0.7
    max_tokens: int = 2048
    
    def __post_init__(self):
        """Validate configuration."""
        self.output_dir = Path(self.output_dir)
        
        if self.output_json:
            self.output_json = Path(self.output_json)
        
        if self.output_report:
            self.output_report = Path(self.output_report)
            
        if self.custom_prompts:
            self.custom_prompts = Path(self.custom_prompts)
            if not self.custom_prompts.exists():
                raise FileNotFoundError(f"Custom prompts file not found: {self.custom_prompts}")
    
    @classmethod
    def from_yaml(cls, path: Path) -> "EvalConfig":
        """Load configuration from YAML file."""
        if not HAS_YAML:
            raise ImportError("pyyaml required for YAML config. Install with: pip3 install pyyaml")
        
        logger.info(f"Loading config from {path}")
        
        with open(path) as f:
            data = yaml.safe_load(f)
        
        return cls(**data)
    
    def to_yaml(self, path: Path) -> None:
        """Save configuration to YAML file."""
        if not HAS_YAML:
            raise ImportError("pyyaml required for YAML config. Install with: pip3 install pyyaml")
        
        logger.info(f"Saving config to {path}")
        
        with open(path, 'w') as f:
            yaml.dump(asdict(self), f, default_flow_style=False)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return asdict(self)


def setup_logging(level: str = "INFO") -> None:
    """Configure logging for the evaluation framework."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
