"""Tests for patterns_generator.generators module."""

from patterns_generator.config import PatternConfig
from patterns_generator.generators import (
    Stroke,
    generate_grid,
    generate_mandala,
    generate_spiral,
)


class TestStrokeDataclass:
    """Tests for Stroke dataclass."""

    def test_stroke_creation(self):
        """Stroke can be created with required fields."""
        stroke = Stroke(x1=0, y1=0, x2=100, y2=100, color="#FF0000", w=2.0)
        assert stroke.x1 == 0
        assert stroke.y1 == 0
        assert stroke.x2 == 100
        assert stroke.y2 == 100
        assert stroke.color == "#FF0000"
        assert stroke.w == 2.0


class TestGenerateSpiral:
    """Tests for generate_spiral function."""

    def test_generate_spiral_returns_nonempty_list(self):
        """generate_spiral returns non-empty list of strokes."""
        config = PatternConfig(
            name="test_spiral",
            pattern_type="spiral",
            center=(400, 300),
            max_radius=250,
            colors=["#FF0000", "#00FF00"],
            params={"spirals": 3, "density": 1.5},
        )
        strokes = generate_spiral(config)
        assert len(strokes) > 0

    def test_generate_spiral_coordinates_in_bounds(self):
        """All stroke coordinates are within canvas bounds."""
        config = PatternConfig(
            name="test_spiral",
            pattern_type="spiral",
            center=(400, 300),
            max_radius=250,
            colors=["#FF0000"],
            params={"spirals": 3, "density": 1.5},
        )
        strokes = generate_spiral(config)

        # Canvas bounds: 0..800 x 0..600 (with some margin for max_radius)
        for stroke in strokes:
            assert 0 <= stroke.x1 <= 800, f"x1={stroke.x1} out of bounds"
            assert 0 <= stroke.y1 <= 600, f"y1={stroke.y1} out of bounds"
            assert 0 <= stroke.x2 <= 800, f"x2={stroke.x2} out of bounds"
            assert 0 <= stroke.y2 <= 600, f"y2={stroke.y2} out of bounds"

    def test_generate_spiral_deterministic(self):
        """generate_spiral is deterministic (same config = same result)."""
        config = PatternConfig(
            name="test_spiral",
            pattern_type="spiral",
            center=(400, 300),
            max_radius=250,
            colors=["#FF0000"],
            params={"spirals": 3, "density": 1.5},
        )
        strokes1 = generate_spiral(config)
        strokes2 = generate_spiral(config)

        assert len(strokes1) == len(strokes2)
        for s1, s2 in zip(strokes1, strokes2):
            assert s1.x1 == s2.x1
            assert s1.y1 == s2.y1
            assert s1.x2 == s2.x2
            assert s1.y2 == s2.y2
            assert s1.color == s2.color


class TestGenerateMandala:
    """Tests for generate_mandala function."""

    def test_generate_mandala_returns_nonempty_list(self):
        """generate_mandala returns non-empty list of strokes."""
        config = PatternConfig(
            name="test_mandala",
            pattern_type="mandala",
            center=(400, 300),
            max_radius=250,
            colors=["#FF0000", "#00FF00", "#0000FF"],
            params={"num_spokes": 36, "layers": 5},
        )
        strokes = generate_mandala(config)
        assert len(strokes) > 0

    def test_generate_mandala_coordinates_in_bounds(self):
        """All stroke coordinates are within canvas bounds."""
        config = PatternConfig(
            name="test_mandala",
            pattern_type="mandala",
            center=(400, 300),
            max_radius=250,
            colors=["#FF0000"],
            params={"num_spokes": 36, "layers": 5},
        )
        strokes = generate_mandala(config)

        for stroke in strokes:
            assert 0 <= stroke.x1 <= 800, f"x1={stroke.x1} out of bounds"
            assert 0 <= stroke.y1 <= 600, f"y1={stroke.y1} out of bounds"
            assert 0 <= stroke.x2 <= 800, f"x2={stroke.x2} out of bounds"
            assert 0 <= stroke.y2 <= 600, f"y2={stroke.y2} out of bounds"

    def test_generate_mandala_deterministic(self):
        """generate_mandala is deterministic."""
        config = PatternConfig(
            name="test_mandala",
            pattern_type="mandala",
            center=(400, 300),
            max_radius=250,
            colors=["#FF0000"],
            params={"num_spokes": 36, "layers": 5},
        )
        strokes1 = generate_mandala(config)
        strokes2 = generate_mandala(config)

        assert len(strokes1) == len(strokes2)
        for s1, s2 in zip(strokes1, strokes2):
            assert s1.x1 == s2.x1
            assert s1.y1 == s2.y1
            assert s1.x2 == s2.x2
            assert s1.y2 == s2.y2


class TestGenerateGrid:
    """Tests for generate_grid function."""

    def test_generate_grid_returns_nonempty_list(self):
        """generate_grid returns non-empty list of strokes."""
        config = PatternConfig(
            name="test_grid",
            pattern_type="grid",
            center=(400, 300),
            max_radius=250,
            colors=["#FF0000", "#0000FF"],
            params={"rows": 10, "cols": 10},
        )
        strokes = generate_grid(config)
        assert len(strokes) > 0

    def test_generate_grid_coordinates_in_bounds(self):
        """All stroke coordinates are within canvas bounds."""
        config = PatternConfig(
            name="test_grid",
            pattern_type="grid",
            center=(400, 300),
            max_radius=250,
            colors=["#FF0000"],
            params={"rows": 10, "cols": 10},
        )
        strokes = generate_grid(config)

        for stroke in strokes:
            assert 0 <= stroke.x1 <= 800, f"x1={stroke.x1} out of bounds"
            assert 0 <= stroke.y1 <= 600, f"y1={stroke.y1} out of bounds"
            assert 0 <= stroke.x2 <= 800, f"x2={stroke.x2} out of bounds"
            assert 0 <= stroke.y2 <= 600, f"y2={stroke.y2} out of bounds"

    def test_generate_grid_deterministic(self):
        """generate_grid is deterministic."""
        config = PatternConfig(
            name="test_grid",
            pattern_type="grid",
            center=(400, 300),
            max_radius=250,
            colors=["#FF0000"],
            params={"rows": 10, "cols": 10},
        )
        strokes1 = generate_grid(config)
        strokes2 = generate_grid(config)

        assert len(strokes1) == len(strokes2)
        for s1, s2 in zip(strokes1, strokes2):
            assert s1.x1 == s2.x1
            assert s1.y1 == s2.y1
            assert s1.x2 == s2.x2
            assert s1.y2 == s2.y2
