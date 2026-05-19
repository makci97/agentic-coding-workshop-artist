"""Tests for palette exports and color formats."""

import re

from palette import GEOMETRIC, MONOCHROME, PALETTES, RAINBOW


def test_palettes_dict_exists():
    """PALETTES dict exists and contains expected keys."""
    assert isinstance(PALETTES, dict)
    assert "geometric" in PALETTES
    assert "rainbow" in PALETTES
    assert "monochrome" in PALETTES


def test_palette_exports():
    """Individual palette exports exist."""
    assert isinstance(GEOMETRIC, list)
    assert isinstance(RAINBOW, list)
    assert isinstance(MONOCHROME, list)


def test_geometric_palette():
    """Geometric palette has 3-5 contrast colors."""
    assert 3 <= len(GEOMETRIC) <= 5
    for color in GEOMETRIC:
        assert re.match(r"^#[0-9A-F]{6}$", color, re.IGNORECASE)


def test_rainbow_palette():
    """Rainbow palette has 6-7 colors."""
    assert 6 <= len(RAINBOW) <= 7
    for color in RAINBOW:
        assert re.match(r"^#[0-9A-F]{6}$", color, re.IGNORECASE)


def test_monochrome_palette():
    """Monochrome palette has 4-5 shades."""
    assert 4 <= len(MONOCHROME) <= 5
    for color in MONOCHROME:
        assert re.match(r"^#[0-9A-F]{6}$", color, re.IGNORECASE)


def test_palettes_match_dict():
    """Exported palettes match PALETTES dict."""
    assert PALETTES["geometric"] == GEOMETRIC
    assert PALETTES["rainbow"] == RAINBOW
    assert PALETTES["monochrome"] == MONOCHROME
