"""Palettes.

Каждая палитра живёт в собственном подпакете: `palette/<palette_name>/`.
Палитра — это набор цветов (и, опционально, правила выбора).
"""

from palette.geometric import COLORS as GEOMETRIC
from palette.monochrome import COLORS as MONOCHROME
from palette.rainbow import COLORS as RAINBOW

PALETTES: dict[str, list[str]] = {
    "geometric": GEOMETRIC,
    "rainbow": RAINBOW,
    "monochrome": MONOCHROME,
}

__all__ = ["PALETTES", "GEOMETRIC", "RAINBOW", "MONOCHROME"]
