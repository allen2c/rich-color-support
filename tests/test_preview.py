"""Tests for preview functions."""

import pytest
from rich.console import Console

from rich_color_support import RichColors, RichColors16, preview, preview_theme
from rich_color_support.themes import THEMES


def _recorded_output(func, *args, **kwargs) -> str:
    console = Console(record=True, force_terminal=True, width=120)
    func(*args, console=console, **kwargs)
    return console.export_text()


def test_preview_full_palette_produces_output():
    text = _recorded_output(preview, RichColors)
    assert text.strip()


def test_preview_named_palette_works():
    text = _recorded_output(preview, RichColors16)
    assert text.strip()


def test_preview_accepts_iterable():
    text = _recorded_output(preview, [RichColors.NAVY_BLUE, RichColors.RED1])
    assert "navy_blue" in text
    assert "red1" in text


@pytest.mark.parametrize("name", list(THEMES.keys()))
def test_preview_theme_each_named_theme(name):
    text = _recorded_output(preview_theme, name)
    assert text.strip()


def test_preview_theme_unknown_name_raises():
    with pytest.raises(ValueError):
        preview_theme("not_a_theme", console=Console(record=True))
