"""Pattern generators for geometric patterns."""

from __future__ import annotations

import math
from dataclasses import dataclass

from patterns_generator.config import PatternConfig


@dataclass
class Stroke:
    """Represents a single stroke segment."""

    x1: float
    y1: float
    x2: float
    y2: float
    color: str
    w: float


def generate_spiral(config: PatternConfig) -> list[Stroke]:
    """Generate spiral pattern.

    Args:
        config: PatternConfig with params.spirals and params.density.

    Returns:
        List of Stroke objects forming the spiral pattern.
    """
    strokes: list[Stroke] = []
    cx, cy = config.center
    max_radius = config.max_radius
    num_spirals = config.params.get("spirals", 3)
    density = config.params.get("density", 1.5)

    colors = config.colors
    color_idx = 0

    for spiral in range(num_spirals):
        angle_offset = (2 * math.pi * spiral) / num_spirals
        points = int(max_radius * density)

        for i in range(points):
            t = i / points
            angle = t * 4 * math.pi + angle_offset  # 2 full rotations
            radius = t * max_radius

            x1 = cx + math.cos(angle) * radius
            y1 = cy + math.sin(angle) * radius

            # Next point
            t_next = (i + 1) / points
            angle_next = t_next * 4 * math.pi + angle_offset
            radius_next = t_next * max_radius

            x2 = cx + math.cos(angle_next) * radius_next
            y2 = cy + math.sin(angle_next) * radius_next

            strokes.append(
                Stroke(
                    x1=x1,
                    y1=y1,
                    x2=x2,
                    y2=y2,
                    color=colors[color_idx % len(colors)],
                    w=config.stroke_width,
                )
            )
            color_idx += 1

    return strokes


def generate_mandala(config: PatternConfig) -> list[Stroke]:
    """Generate mandala pattern (radially symmetric design).

    Args:
        config: PatternConfig with params.num_spokes and params.layers.

    Returns:
        List of Stroke objects forming the mandala pattern.
    """
    strokes: list[Stroke] = []
    cx, cy = config.center
    max_radius = config.max_radius
    num_spokes = config.params.get("num_spokes", 36)
    num_layers = config.params.get("layers", 5)

    colors = config.colors

    # Generate spokes
    for spoke in range(num_spokes):
        angle = (2 * math.pi * spoke) / num_spokes + config.rotation_angle

        for layer in range(1, num_layers + 1):
            radius = (layer / num_layers) * max_radius
            x2 = cx + math.cos(angle) * radius
            y2 = cy + math.sin(angle) * radius

            # Inner point (from center or previous layer)
            if layer == 1:
                x1, y1 = cx, cy
            else:
                prev_radius = ((layer - 1) / num_layers) * max_radius
                x1 = cx + math.cos(angle) * prev_radius
                y1 = cy + math.sin(angle) * prev_radius

            color_idx = (spoke + layer) % len(colors)
            strokes.append(
                Stroke(
                    x1=x1,
                    y1=y1,
                    x2=x2,
                    y2=y2,
                    color=colors[color_idx],
                    w=config.stroke_width,
                )
            )

    return strokes


def generate_grid(config: PatternConfig) -> list[Stroke]:
    """Generate grid pattern.

    Args:
        config: PatternConfig with params.rows and params.cols.
                config.size should be (width, height) or use max_radius.

    Returns:
        List of Stroke objects forming the grid pattern.
    """
    strokes: list[Stroke] = []
    cx, cy = config.center

    # Get grid dimensions
    if hasattr(config, "size") and config.params.get("size"):
        width, height = config.params["size"]
    else:
        # Default to 800x600 or use max_radius
        width = config.params.get("size", [800, 600])[0]
        height = config.params.get("size", [800, 600])[1]

    num_rows = config.params.get("rows", 10)
    num_cols = config.params.get("cols", 10)

    colors = config.colors
    color_idx = 0

    # Calculate grid spacing
    cell_width = width / (num_cols + 1)
    cell_height = height / (num_rows + 1)

    # Left and top boundaries
    left = cx - width / 2
    top = cy - height / 2

    # Generate horizontal lines
    for row in range(num_rows + 1):
        y = top + row * cell_height
        x_start = left
        x_end = left + width

        strokes.append(
            Stroke(
                x1=x_start,
                y1=y,
                x2=x_end,
                y2=y,
                color=colors[color_idx % len(colors)],
                w=config.stroke_width,
            )
        )
        color_idx += 1

    # Generate vertical lines
    for col in range(num_cols + 1):
        x = left + col * cell_width
        y_start = top
        y_end = top + height

        strokes.append(
            Stroke(
                x1=x,
                y1=y_start,
                x2=x,
                y2=y_end,
                color=colors[color_idx % len(colors)],
                w=config.stroke_width,
            )
        )
        color_idx += 1

    return strokes
