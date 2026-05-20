"""Print palette and theme previews to a Rich Console."""

from typing import Iterable

from rich.columns import Columns
from rich.console import Console
from rich.text import Text

from rich_color_support._palettes import RichColors, RichColorsBase
from rich_color_support.semantic import SemanticColors
from rich_color_support.themes import THEMES

_SAMPLE_TEXT = "The quick brown fox"


def preview(
    palette: type[RichColorsBase] | Iterable[RichColorsBase] = RichColors,
    *,
    columns: int = 4,
    console: Console | None = None,
) -> None:
    """Print each color's name in its own color, arranged in a grid."""
    console = console or Console()
    swatches = [Text(m.value, style=m.value) for m in list(palette)]
    console.print(Columns(swatches, equal=True, expand=True, column_first=True))


def preview_theme(
    theme_name: str = "default",
    *,
    console: Console | None = None,
) -> None:
    """Print one sample line per SemanticColors role for the named theme."""
    if theme_name not in THEMES:
        raise ValueError(
            f"Unknown theme: {theme_name!r}; "
            f"expected one of {sorted(THEMES.keys())}"
        )

    theme = THEMES[theme_name]
    console = console or Console(theme=theme)
    console.push_theme(theme)
    try:
        for role in SemanticColors:
            console.print(f"[{role.value}]{role.value:<9}: {_SAMPLE_TEXT}[/]")
    finally:
        console.pop_theme()
