from rich.console import Console
from rich.text import Text


def test_rich_colors_valid(console: Console):
    from rich_color_support import (
        RichColors,
        RichColors8,
        RichColors16,
        RichColors32,
        RichColors64,
    )

    for colors in [RichColors, RichColors8, RichColors16, RichColors32, RichColors64]:
        for color in colors:
            console.print(Text(f"{color.value}"), style=color)


def test_rich_color_rotator(console: Console):
    from rich_color_support import RichColorRotator

    size = 200
    rotator = RichColorRotator(size=size)
    for idx, _ in enumerate(range(size * 2)):
        color_name = rotator.pick().value
        console.print(Text(f"{idx}. {color_name}"), style=color_name)
