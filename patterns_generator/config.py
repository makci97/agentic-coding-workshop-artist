"""Configuration loader for pattern JSON configs."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class PatternConfig:
    """Configuration for a pattern generator."""

    name: str
    pattern_type: str
    center: tuple[int, int]
    max_radius: int
    colors: list[str]
    stroke_width: float = 2.0
    rotation_angle: float = 0.0
    params: dict[str, Any] = field(default_factory=dict)


class ConfigValidationError(ValueError):
    """Raised when pattern config validation fails."""


def validate_config(config: dict[str, Any]) -> PatternConfig:
    """Validate pattern config dictionary and return PatternConfig.

    Args:
        config: Raw config dictionary from JSON.

    Returns:
        PatternConfig dataclass instance.

    Raises:
        ConfigValidationError: If required fields are missing or invalid.
    """
    # Check required fields
    required_fields = ["name", "pattern_type", "colors"]
    for field_name in required_fields:
        if field_name not in config:
            raise ConfigValidationError(f"Missing required field: {field_name}")

    # Validate types
    if not isinstance(config["name"], str):
        raise ConfigValidationError("Field 'name' must be a string")
    if not isinstance(config["pattern_type"], str):
        raise ConfigValidationError("Field 'pattern_type' must be a string")
    if not isinstance(config["colors"], list):
        raise ConfigValidationError("Field 'colors' must be a list")
    if not all(isinstance(c, str) for c in config["colors"]):
        raise ConfigValidationError("All colors must be strings")

    # Build config with defaults
    return PatternConfig(
        name=config["name"],
        pattern_type=config["pattern_type"],
        center=tuple(config.get("center", [400, 300])),  # type: ignore[arg-type]
        max_radius=config.get("max_radius", 250),
        colors=config["colors"],
        stroke_width=config.get("stroke_width", 2.0),
        rotation_angle=config.get("rotation_angle", 0.0),
        params=config.get("params", {}),
    )


def load_pattern(path: str | Path) -> PatternConfig:
    """Load and validate pattern config from JSON file.

    Args:
        path: Path to JSON config file.

    Returns:
        PatternConfig dataclass instance.

    Raises:
        FileNotFoundError: If config file doesn't exist.
        json.JSONDecodeError: If file is not valid JSON.
        ConfigValidationError: If config validation fails.
    """
    path = Path(path)
    with path.open("r", encoding="utf-8") as f:
        config = json.load(f)
    return validate_config(config)
