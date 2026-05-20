# Changelog

All notable changes to this project are documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.2.0] — 2026-05-20

### Added
- `SemanticColors` enum of 15 UI/log role names (`SUCCESS`, `ERROR`,
  `WARNING`, `INFO`, `DEBUG`, `CRITICAL`, `MUTED`, `HIGHLIGHT`, `PRIMARY`,
  `SECONDARY`, `PROMPT`, `HINT`, `CODE`, `LINK`, `HEADING`).
- Eight Rich `Theme` factories: `default_theme`, `dark_theme`,
  `light_theme`, `high_contrast_theme`, `monochrome_theme`,
  `colorblind_theme` (Okabe-Ito inspired), `pastel_theme`, `monokai_theme`.
- `build_theme()` for partial-override custom themes.
- `THEMES` registry dict mapping theme names to pre-built `Theme` instances.
- `filter_colors()` for selecting palette members by hue, brightness,
  temperature, and saturation.
- `preview()` and `preview_theme()` helpers.
- `python -m rich_color_support` CLI with `preview`, `themes`, `theme`
  subcommands.
- `py.typed` marker (PEP 561) — type information now ships with the package.

### Changed
- Internal restructure: the public package is split into focused modules
  (`_palettes`, `_rotator`, `semantic`, `themes`, `filters`, `preview`,
  `__main__`). All v0.1.0 public imports continue to work unchanged.

## [0.1.0]

### Added
- `RichColorsBase`, `RichColors`, `RichColors8`, `RichColors16`,
  `RichColors32`, `RichColors64` palettes.
- `get_color_set(size)` palette picker.
- `RichColorRotator` shuffled cycle utility.
