"""CLI entry point for rich_color_support.

Subcommands:
    preview   Print a palette (optionally filtered) as a grid of swatches.
    themes    List the eight built-in theme names.
    theme     Preview a single theme; --demo also renders a logger sample.
"""

import argparse
import sys

from rich.console import Console

from rich_color_support._palettes import RichColors
from rich_color_support._rotator import get_color_set
from rich_color_support.filters import filter_colors
from rich_color_support.preview import preview, preview_theme
from rich_color_support.semantic import SemanticColors
from rich_color_support.themes import THEMES

_DEMO_LINES = [
    (SemanticColors.DEBUG, "Connecting to database..."),
    (SemanticColors.INFO, "Listening on http://localhost:8080"),
    (SemanticColors.SUCCESS, "Request handled in 12ms"),
    (SemanticColors.WARNING, "Slow query detected (320ms)"),
    (SemanticColors.ERROR, "Failed to enqueue job"),
    (SemanticColors.CRITICAL, "Database connection lost"),
]


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "preview":
        return _cmd_preview(args)
    if args.command == "themes":
        return _cmd_themes()
    if args.command == "theme":
        return _cmd_theme(args)
    parser.print_help()
    return 2


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m rich_color_support",
        description="Inspect rich-color-support palettes and themes.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_prev = sub.add_parser("preview", help="Preview a palette as a grid.")
    p_prev.add_argument(
        "--size",
        type=int,
        default=None,
        help="Use get_color_set(SIZE) instead of the full palette.",
    )
    p_prev.add_argument("--hue", default=None)
    p_prev.add_argument("--brightness", default=None)
    p_prev.add_argument("--temperature", default=None)
    p_prev.add_argument("--saturation", default=None)
    p_prev.add_argument("--columns", type=int, default=4)

    sub.add_parser("themes", help="List the eight built-in theme names.")

    p_theme = sub.add_parser("theme", help="Preview a single theme.")
    p_theme.add_argument("name", help="Theme name (e.g. dark, light, monokai).")
    p_theme.add_argument(
        "--demo",
        action="store_true",
        help="Also render a logger-style sample.",
    )

    return parser


def _cmd_preview(args: argparse.Namespace) -> int:
    base = get_color_set(args.size) if args.size else list(RichColors)
    try:
        filtered = filter_colors(
            base,
            hue=args.hue,
            brightness=args.brightness,
            temperature=args.temperature,
            saturation=args.saturation,
        )
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    preview(filtered, columns=args.columns)
    return 0


def _cmd_themes() -> int:
    for name in THEMES:
        print(name)
    return 0


def _cmd_theme(args: argparse.Namespace) -> int:
    if args.name not in THEMES:
        print(
            f"Unknown theme: {args.name!r}; expected one of {sorted(THEMES.keys())}",
            file=sys.stderr,
        )
        return 2

    preview_theme(args.name)

    if args.demo:
        console = Console(theme=THEMES[args.name])
        console.print()
        console.rule("demo log output")
        for role, msg in _DEMO_LINES:
            console.print(f"[{role.value}]{role.value.upper():<8}[/] {msg}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
