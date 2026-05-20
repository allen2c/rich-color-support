"""Tests for the SemanticColors enum."""

from rich_color_support import SemanticColors
from rich_color_support._palettes import RichColorsBase

EXPECTED_ROLES = {
    "SUCCESS",
    "ERROR",
    "WARNING",
    "INFO",
    "DEBUG",
    "CRITICAL",
    "MUTED",
    "HIGHLIGHT",
    "PRIMARY",
    "SECONDARY",
    "PROMPT",
    "HINT",
    "CODE",
    "LINK",
    "HEADING",
}


def test_member_set():
    assert {m.name for m in SemanticColors} == EXPECTED_ROLES


def test_values_are_lowercase_role_names():
    for member in SemanticColors:
        assert member.value == member.name.lower()


def test_inherits_rich_colors_base():
    assert issubclass(SemanticColors, RichColorsBase)
    for member in SemanticColors:
        assert isinstance(member, RichColorsBase)


def test_usable_as_markup_tag():
    s = f"[{SemanticColors.SUCCESS}]ok[/]"
    assert s == "[success]ok[/]"
