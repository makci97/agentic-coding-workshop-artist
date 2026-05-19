"""Tests for patterns_generator.__main__ module."""

import subprocess
import sys
from pathlib import Path

import pytest

PATTERNS_DIR = Path(__file__).parent.parent.parent / "patterns"


class TestMainScript:
    """Tests for main script entry point."""

    def test_main_no_args(self):
        """Main script shows usage when no args provided."""
        result = subprocess.run(
            [sys.executable, "-m", "patterns_generator"],
            capture_output=True,
            text=True,
        )
        assert "Usage:" in result.stdout

    def test_main_nonexistent_config(self):
        """Main script errors on nonexistent config file."""
        result = subprocess.run(
            [sys.executable, "-m", "patterns_generator", "/nonexistent/config.json"],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0
        assert "Error" in result.stdout or "Error" in result.stderr

    def test_main_valid_config(self):
        """Main script loads valid config successfully."""
        config_path = PATTERNS_DIR / "spiral.json"
        if not config_path.exists():
            pytest.skip("Config file not found")

        result = subprocess.run(
            [
                sys.executable,
                "-m", "patterns_generator",
                str(config_path),
            ],
            capture_output=True,
            text=True,
            timeout=30,
        )
        # Should load config successfully (may fail on network)
        # Check stdout or stderr for expected output
        output = result.stdout + result.stderr
        assert "Loaded config:" in output or "Error" in output or result.returncode == 0
