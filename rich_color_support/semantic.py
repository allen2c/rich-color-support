"""Semantic role names usable as Rich theme keys and markup tags."""

from rich_color_support._palettes import RichColorsBase


class SemanticColors(RichColorsBase):
    """Semantic UI/log role names.

    Each member's value is the lowercase role name, which doubles as the
    Rich theme key and markup tag. See themes.py for role-to-color mappings.
    """

    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"
    CRITICAL = "critical"
    MUTED = "muted"
    HIGHLIGHT = "highlight"
    PRIMARY = "primary"
    SECONDARY = "secondary"
    PROMPT = "prompt"
    HINT = "hint"
    CODE = "code"
    LINK = "link"
    HEADING = "heading"
