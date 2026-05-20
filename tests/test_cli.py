"""End-to-end CLI tests via subprocess."""

import subprocess
import sys


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "rich_color_support", *args],
        capture_output=True,
        text=True,
    )


def test_no_args_shows_help_and_exits_nonzero():
    result = _run()
    assert result.returncode != 0
    assert "usage" in (result.stdout + result.stderr).lower()


def test_preview_default_palette():
    result = _run("preview")
    assert result.returncode == 0
    assert result.stdout.strip()


def test_preview_with_size():
    result = _run("preview", "--size", "16")
    assert result.returncode == 0


def test_preview_with_filter():
    result = _run("preview", "--hue", "blue")
    assert result.returncode == 0


def test_themes_lists_eight_names():
    result = _run("themes")
    assert result.returncode == 0
    for name in [
        "default",
        "dark",
        "light",
        "high_contrast",
        "monochrome",
        "colorblind",
        "pastel",
        "monokai",
    ]:
        assert name in result.stdout


def test_theme_specific_name():
    result = _run("theme", "dark")
    assert result.returncode == 0


def test_theme_unknown_name_errors():
    result = _run("theme", "nonsense")
    assert result.returncode != 0


def test_theme_demo_flag():
    result = _run("theme", "dark", "--demo")
    assert result.returncode == 0
