"""Tests for filter_colors and the classification table."""

import pytest

from rich_color_support import RichColors, RichColors8, filter_colors
from rich_color_support.filters import _CLASSIFICATION


def test_classification_covers_every_rich_colors_member():
    missing = [c.value for c in RichColors if c.value not in _CLASSIFICATION]
    assert missing == [], f"Classification table missing entries: {missing}"


def test_no_filter_returns_full_palette_as_list():
    out = filter_colors(RichColors)
    assert isinstance(out, list)
    assert len(out) == len(list(RichColors))


def test_single_criterion_returns_subset():
    blues = filter_colors(RichColors, hue="blue")
    assert len(blues) > 0
    assert len(blues) < len(list(RichColors))
    for c in blues:
        assert _CLASSIFICATION[c.value].hue == "blue"


def test_multi_criterion_and_combines():
    dark_blues = filter_colors(RichColors, hue="blue", brightness="dark")
    for c in dark_blues:
        attrs = _CLASSIFICATION[c.value]
        assert attrs.hue == "blue"
        assert attrs.brightness == "dark"


def test_invalid_literal_raises_value_error():
    with pytest.raises(ValueError):
        filter_colors(RichColors, hue="ultraviolet")  # type: ignore[arg-type]


def test_accepts_iterable_for_chaining():
    dark = filter_colors(RichColors, brightness="dark")
    dark_blues = filter_colors(dark, hue="blue")
    assert all(_CLASSIFICATION[c.value].hue == "blue" for c in dark_blues)


def test_filter_works_on_smaller_palettes():
    # RichColors8 contains a few values (e.g. "white") not present in the
    # descriptive RichColors palette; filter_colors silently excludes them
    # rather than raising.
    out = filter_colors(RichColors8)
    assert isinstance(out, list)
    assert all(c.value in _CLASSIFICATION for c in out)
