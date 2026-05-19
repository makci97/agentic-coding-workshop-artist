"""Tests for pattern JSON configs."""

import json
import re
from pathlib import Path


PATTERNS_DIR = Path(__file__).parent.parent.parent / "patterns"


def test_patterns_dir_exists():
    """patterns/ directory exists."""
    assert PATTERNS_DIR.exists()


def test_spiral_config_exists():
    """spiral.json exists."""
    assert (PATTERNS_DIR / "spiral.json").exists()


def test_mandala_config_exists():
    """mandala.json exists."""
    assert (PATTERNS_DIR / "mandala.json").exists()


def test_grid_config_exists():
    """grid.json exists."""
    assert (PATTERNS_DIR / "grid.json").exists()


def load_config(name: str) -> dict:
    """Load pattern config by name."""
    with open(PATTERNS_DIR / f"{name}.json") as f:
        return json.load(f)


def is_hex_color(color: str) -> bool:
    """Check if string is valid hex color."""
    return bool(re.match(r"^#[0-9A-F]{6}$", color, re.IGNORECASE))


def test_spiral_config():
    """spiral.json has required fields."""
    config = load_config("spiral")
    assert config["name"] == "spiral"
    assert config["pattern_type"] == "spiral"
    assert "center" in config
    assert "max_radius" in config
    assert "colors" in config
    assert "stroke_width" in config
    assert "params" in config
    assert "spirals" in config["params"]
    assert "density" in config["params"]
    assert all(is_hex_color(c) for c in config["colors"])


def test_mandala_config():
    """mandala.json has required fields."""
    config = load_config("mandala")
    assert config["name"] == "mandala"
    assert config["pattern_type"] == "mandala"
    assert "center" in config
    assert "max_radius" in config
    assert "colors" in config
    assert "stroke_width" in config
    assert "params" in config
    assert "num_spokes" in config["params"]
    assert "layers" in config["params"]
    assert all(is_hex_color(c) for c in config["colors"])


def test_grid_config():
    """grid.json has required fields."""
    config = load_config("grid")
    assert config["name"] == "grid"
    assert config["pattern_type"] == "grid"
    assert "center" in config
    assert "size" in config
    assert "colors" in config
    assert "stroke_width" in config
    assert "params" in config
    assert "rows" in config["params"]
    assert "cols" in config["params"]
    assert all(is_hex_color(c) for c in config["colors"])
