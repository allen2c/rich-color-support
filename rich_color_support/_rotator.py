"""Color-set picker and randomized rotator."""

import logging
import random
import typing

from rich_color_support._palettes import (
    RichColors,
    RichColors8,
    RichColors16,
    RichColors32,
    RichColors64,
    RichColorsBase,
)

logger = logging.getLogger(__name__)


def get_color_set(size: int) -> typing.List[RichColorsBase]:
    """Return a color set of the requested approximate size."""
    if size > len(RichColors64):
        return list(RichColors)
    elif size == 64 or size > len(RichColors32):
        return list(RichColors64)
    elif size == 32 or size > len(RichColors16):
        return list(RichColors32)
    elif size == 16 or size > len(RichColors8):
        return list(RichColors16)
    elif size == 8:
        return list(RichColors8)
    elif size > 0:
        return random.sample(list(RichColors8), size)
    else:
        logger.warning(f"Invalid size: {size}, returning 8 colors")
        return list(RichColors8)


class RichColorRotator:
    """Cycle through a shuffled color set, reshuffling when exhausted."""

    def __init__(self, size: int = 16):
        self.size = size
        self.colors = get_color_set(size)
        random.shuffle(self.colors)

    def pick(self) -> RichColorsBase:
        if len(self.colors) == 0:
            self.colors = get_color_set(self.size)
            random.shuffle(self.colors)
        return self.colors.pop()
