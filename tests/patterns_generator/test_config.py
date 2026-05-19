"""Tests for patterns_generator.config module."""

import json
import tempfile
from pathlib import Path

import pytest

from patterns_generator.config import (
    ConfigValidationError,
    PatternConfig,
    load_pattern,
    validate_config,
)


class TestPatternConfigDataclass:
    """Tests for PatternConfig dataclass."""

    def test_pattern_config_creation(self):
        """PatternConfig can be created with required fields."""
        config = PatternConfig(
            name="test_pattern",
            pattern_type="spiral",
            center=(400, 300),
            max_radius=250,
            colors=["#FF0000", "#00FF00"],
        )
        assert config.name == "test_pattern"
        assert config.pattern_type == "spiral"
        assert config.center == (400, 300)
        assert config.max_radius == 250
        assert config.colors == ["#FF0000", "#00FF00"]
        assert config.stroke_width == 2.0  # default
        assert config.rotation_angle == 0.0  # default
        assert config.params == {}  # default


class TestValidateConfig:
    """Tests for validate_config function."""

    def test_valid_config(self):
        """Valid config returns PatternConfig."""
        config_dict = {
            "name": "test",
            "pattern_type": "spiral",
            "center": [400, 300],
            "max_radius": 250,
            "colors": ["#FF0000"],
        }
        result = validate_config(config_dict)
        assert isinstance(result, PatternConfig)
        assert result.name == "test"

    def test_missing_name(self):
        """Missing 'name' field raises ConfigValidationError."""
        config_dict = {
            "pattern_type": "spiral",
            "colors": ["#FF0000"],
        }
        with pytest.raises(ConfigValidationError, match="Missing required field: name"):
            validate_config(config_dict)

    def test_missing_pattern_type(self):
        """Missing 'pattern_type' field raises ConfigValidationError."""
        config_dict = {
            "name": "test",
            "colors": ["#FF0000"],
        }
        with pytest.raises(ConfigValidationError, match="Missing required field: pattern_type"):
            validate_config(config_dict)

    def test_missing_colors(self):
        """Missing 'colors' field raises ConfigValidationError."""
        config_dict = {
            "name": "test",
            "pattern_type": "spiral",
        }
        with pytest.raises(ConfigValidationError, match="Missing required field: colors"):
            validate_config(config_dict)

    def test_invalid_name_type(self):
        """Non-string 'name' raises ConfigValidationError."""
        config_dict = {
            "name": 123,
            "pattern_type": "spiral",
            "colors": ["#FF0000"],
        }
        with pytest.raises(ConfigValidationError, match="'name' must be a string"):
            validate_config(config_dict)

    def test_invalid_colors_type(self):
        """Non-list 'colors' raises ConfigValidationError."""
        config_dict = {
            "name": "test",
            "pattern_type": "spiral",
            "colors": "#FF0000",  # string instead of list
        }
        with pytest.raises(ConfigValidationError, match="'colors' must be a list"):
            validate_config(config_dict)

    def test_invalid_color_in_list(self):
        """Non-string color in list raises ConfigValidationError."""
        config_dict = {
            "name": "test",
            "pattern_type": "spiral",
            "colors": ["#FF0000", 123],
        }
        with pytest.raises(ConfigValidationError, match="colors must be strings"):
            validate_config(config_dict)

    def test_default_values(self):
        """Missing optional fields use default values."""
        config_dict = {
            "name": "test",
            "pattern_type": "spiral",
            "colors": ["#FF0000"],
        }
        result = validate_config(config_dict)
        assert result.stroke_width == 2.0
        assert result.rotation_angle == 0.0
        assert result.params == {}


class TestLoadPattern:
    """Tests for load_pattern function."""

    def test_load_valid_pattern(self):
        """load_pattern returns PatternConfig for valid file."""
        config_data = {
            "name": "test_pattern",
            "pattern_type": "spiral",
            "center": [400, 300],
            "max_radius": 250,
            "colors": ["#FF0000", "#00FF00"],
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(config_data, f)
            f.flush()
            result = load_pattern(f.name)
        assert isinstance(result, PatternConfig)
        assert result.name == "test_pattern"

    def test_load_nonexistent_file(self):
        """load_pattern raises FileNotFoundError for missing file."""
        with pytest.raises(FileNotFoundError):
            load_pattern("/nonexistent/path/config.json")

    def test_load_invalid_json(self):
        """load_pattern raises JSONDecodeError for invalid JSON."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            f.write("{ invalid json }")
            f.flush()
            with pytest.raises(json.JSONDecodeError):
                load_pattern(f.name)

    def test_load_invalid_config(self):
        """load_pattern raises ConfigValidationError for invalid config."""
        config_data = {
            "name": "test",
            # missing required fields
        }
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(config_data, f)
            f.flush()
            with pytest.raises(ConfigValidationError):
                load_pattern(f.name)
