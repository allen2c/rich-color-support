"""Backwards-compatibility tests guarding v0.1.0 public API."""

from rich_color_support import (
    RichColorRotator,
    RichColors,
    RichColors8,
    RichColors16,
    RichColors32,
    RichColors64,
    RichColorsBase,
    get_color_set,
)


def test_v010_symbols_importable():
    assert RichColorsBase is not None
    assert RichColors is not None
    assert RichColors8 is not None
    assert RichColors16 is not None
    assert RichColors32 is not None
    assert RichColors64 is not None
    assert callable(get_color_set)
    assert RichColorRotator is not None


def test_v010_enum_sizes():
    assert len(RichColors8) == 8
    assert len(RichColors16) == 16
    assert len(RichColors32) == 32
    assert len(RichColors64) == 64
    assert len(RichColors) >= 100


def test_v010_get_color_set_returns_list():
    out = get_color_set(8)
    assert isinstance(out, list)
    assert len(out) == 8


def test_v010_rotator_pick_returns_str():
    rotator = RichColorRotator(8)
    pick = rotator.pick()
    assert isinstance(pick, str)
