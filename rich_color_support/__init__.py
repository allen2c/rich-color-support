"""Rich-friendly curated color palettes, semantic colors, and themes."""

from rich_color_support._palettes import (
    RichColors,
    RichColors8,
    RichColors16,
    RichColors32,
    RichColors64,
    RichColorsBase,
)
from rich_color_support._rotator import RichColorRotator, get_color_set
from rich_color_support.filters import filter_colors
from rich_color_support.preview import preview, preview_theme
from rich_color_support.semantic import SemanticColors
from rich_color_support.themes import (
    THEMES,
    build_theme,
    colorblind_theme,
    dark_theme,
    default_theme,
    high_contrast_theme,
    light_theme,
    monochrome_theme,
    monokai_theme,
    pastel_theme,
)

__version__ = "0.2.0"

__all__ = [
    "RichColorsBase",
    "RichColors",
    "RichColors8",
    "RichColors16",
    "RichColors32",
    "RichColors64",
    "get_color_set",
    "RichColorRotator",
    "SemanticColors",
    "build_theme",
    "default_theme",
    "dark_theme",
    "light_theme",
    "high_contrast_theme",
    "monochrome_theme",
    "colorblind_theme",
    "pastel_theme",
    "monokai_theme",
    "THEMES",
    "filter_colors",
    "preview",
    "preview_theme",
    "__version__",
]
