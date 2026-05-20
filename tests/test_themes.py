"""Tests for theme factories."""

import pytest
from rich.console import Console
from rich.theme import Theme

from rich_color_support import (
    SemanticColors,
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

ALL_ROLES = {m.value for m in SemanticColors}


def test_dark_theme_returns_theme():
    assert isinstance(dark_theme(), Theme)


def test_dark_theme_covers_all_roles():
    theme = dark_theme()
    for role in ALL_ROLES:
        assert role in theme.styles, f"dark_theme missing role: {role}"


def test_default_theme_is_dark():
    assert {k: str(v) for k, v in default_theme().styles.items()} == {
        k: str(v) for k, v in dark_theme().styles.items()
    }


def test_factories_return_fresh_instances():
    a, b = dark_theme(), dark_theme()
    assert a is not b


def test_console_with_dark_theme_renders_without_error():
    console = Console(theme=dark_theme(), record=True, force_terminal=True)
    for role in ALL_ROLES:
        console.print(f"[{role}]sample[/]")
    assert console.export_text()


def test_build_theme_partial_override_falls_back_to_dark():
    custom = build_theme({"success": "magenta1"})
    assert "magenta1" in str(custom.styles["success"])
    assert str(custom.styles["error"]) == str(dark_theme().styles["error"])


def test_build_theme_accepts_semantic_color_keys():
    custom = build_theme({SemanticColors.WARNING: "red3"})
    assert "red3" in str(custom.styles["warning"])


ALL_FACTORIES = [
    dark_theme,
    default_theme,
    light_theme,
    high_contrast_theme,
    monochrome_theme,
    colorblind_theme,
    pastel_theme,
    monokai_theme,
]


@pytest.mark.parametrize("factory", ALL_FACTORIES)
def test_factory_returns_theme(factory):
    assert isinstance(factory(), Theme)


@pytest.mark.parametrize("factory", ALL_FACTORIES)
def test_factory_covers_all_roles(factory):
    theme = factory()
    for role in ALL_ROLES:
        assert role in theme.styles, f"{factory.__name__} missing role: {role}"


@pytest.mark.parametrize("factory", ALL_FACTORIES)
def test_console_renders_without_error(factory):
    console = Console(theme=factory(), record=True, force_terminal=True)
    for role in ALL_ROLES:
        console.print(f"[{role}]sample[/]")
    assert console.export_text()
