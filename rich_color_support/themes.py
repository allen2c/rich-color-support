"""Rich Theme factories for SemanticColors-keyed UI / log styling."""

from typing import Literal, Mapping

from rich.theme import Theme

from rich_color_support.semantic import SemanticColors

ThemeName = Literal[
    "default",
    "dark",
    "light",
    "high_contrast",
    "monochrome",
    "colorblind",
    "pastel",
    "monokai",
]

_DARK_MAPPING: dict[str, str] = {
    "success": "green1",
    "error": "red1",
    "warning": "gold1",
    "info": "deep_sky_blue1",
    "debug": "grey50",
    "critical": "bright_red bold",
    "muted": "grey42",
    "highlight": "gold3",
    "primary": "royal_blue1",
    "secondary": "medium_purple1",
    "prompt": "cornflower_blue",
    "hint": "grey70",
    "code": "chartreuse1",
    "link": "deep_sky_blue1 underline",
    "heading": "white bold",
}

_LIGHT_MAPPING: dict[str, str] = {
    "success": "green4",
    "error": "red3",
    "warning": "orange3",
    "info": "deep_sky_blue4",
    "debug": "grey42",
    "critical": "dark_red bold",
    "muted": "grey70",
    "highlight": "dark_goldenrod",
    "primary": "dark_blue",
    "secondary": "purple4",
    "prompt": "blue3",
    "hint": "grey50",
    "code": "dark_green",
    "link": "dark_blue underline",
    "heading": "grey0 bold",
}

_HIGH_CONTRAST_MAPPING: dict[str, str] = {
    "success": "green1 bold",
    "error": "bright_red bold",
    "warning": "yellow1 bold",
    "info": "cyan1 bold",
    "debug": "white",
    "critical": "bright_red bold reverse",
    "muted": "grey70",
    "highlight": "yellow1 bold",
    "primary": "blue1 bold",
    "secondary": "magenta1 bold",
    "prompt": "white bold",
    "hint": "white",
    "code": "chartreuse1 bold",
    "link": "cyan1 bold underline",
    "heading": "white bold reverse",
}

_MONOCHROME_MAPPING: dict[str, str] = {
    "success": "bold",
    "error": "bold reverse",
    "warning": "italic",
    "info": "none",
    "debug": "dim",
    "critical": "bold reverse",
    "muted": "dim",
    "highlight": "bold underline",
    "primary": "bold",
    "secondary": "italic",
    "prompt": "bold",
    "hint": "dim italic",
    "code": "italic",
    "link": "underline",
    "heading": "bold underline",
}

_COLORBLIND_MAPPING: dict[str, str] = {
    "success": "spring_green3",
    "error": "orange_red1 bold",
    "warning": "dark_orange",
    "info": "deep_sky_blue2",
    "debug": "grey50",
    "critical": "orange_red1 bold reverse",
    "muted": "grey42",
    "highlight": "yellow1",
    "primary": "blue3",
    "secondary": "medium_orchid",
    "prompt": "deep_sky_blue2",
    "hint": "grey70",
    "code": "spring_green3",
    "link": "blue3 underline",
    "heading": "white bold",
}

_PASTEL_MAPPING: dict[str, str] = {
    "success": "pale_green3",
    "error": "light_coral",
    "warning": "light_goldenrod3",
    "info": "light_steel_blue",
    "debug": "grey58",
    "critical": "indian_red bold",
    "muted": "grey50",
    "highlight": "navajo_white3",
    "primary": "light_steel_blue3",
    "secondary": "medium_purple3",
    "prompt": "light_sky_blue3",
    "hint": "grey66",
    "code": "dark_sea_green",
    "link": "light_steel_blue underline",
    "heading": "light_steel_blue1 bold",
}

_MONOKAI_MAPPING: dict[str, str] = {
    "success": "green_yellow",
    "error": "deep_pink2 bold",
    "warning": "dark_orange",
    "info": "deep_sky_blue1",
    "debug": "grey42",
    "critical": "deep_pink2 bold reverse",
    "muted": "grey42",
    "highlight": "khaki1",
    "primary": "deep_sky_blue1",
    "secondary": "medium_purple1",
    "prompt": "green_yellow",
    "hint": "grey50",
    "code": "green_yellow",
    "link": "deep_sky_blue1 underline",
    "heading": "grey93 bold",
}


def build_theme(mapping: Mapping[SemanticColors | str, str]) -> Theme:
    """Build a Rich Theme from a {role: style} mapping.

    Missing roles fall back to dark_theme's value so partial overrides are safe.
    """
    merged = dict(_DARK_MAPPING)
    for key, style in mapping.items():
        merged[str(key)] = style
    return Theme(merged)


def dark_theme() -> Theme:
    """Sensible defaults for dark terminals."""
    return _make_theme(_DARK_MAPPING)


def default_theme() -> Theme:
    """Alias of dark_theme; used when no preference is expressed."""
    return dark_theme()


def light_theme() -> Theme:
    """Sensible defaults for light terminal backgrounds."""
    return _make_theme(_LIGHT_MAPPING)


def high_contrast_theme() -> Theme:
    """Maximum-contrast palette for accessibility."""
    return _make_theme(_HIGH_CONTRAST_MAPPING)


def monochrome_theme() -> Theme:
    """Style-only theme (bold/italic/underline/dim) without color."""
    return _make_theme(_MONOCHROME_MAPPING)


def colorblind_theme() -> Theme:
    """Okabe-Ito-inspired palette safe across common color blindness types."""
    return _make_theme(_COLORBLIND_MAPPING)


def pastel_theme() -> Theme:
    """Low-saturation palette for long-running scripts."""
    return _make_theme(_PASTEL_MAPPING)


def monokai_theme() -> Theme:
    """Monokai-inspired high-saturation dark palette."""
    return _make_theme(_MONOKAI_MAPPING)


def _make_theme(mapping: dict[str, str]) -> Theme:
    # Fresh dict per call so callers cannot mutate the module-level mapping
    # through the returned Theme instance.
    return Theme(dict(mapping))


THEMES: dict[str, Theme] = {
    "default": default_theme(),
    "dark": dark_theme(),
    "light": light_theme(),
    "high_contrast": high_contrast_theme(),
    "monochrome": monochrome_theme(),
    "colorblind": colorblind_theme(),
    "pastel": pastel_theme(),
    "monokai": monokai_theme(),
}
