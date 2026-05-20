# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project

`rich-color-support` — a small Python library that provides curated color palettes (as `StrEnum` classes) for use with the [Rich](https://github.com/Textualize/rich) terminal library, plus utilities for picking, rotating, and (from v0.2.0) theming colors.

- Package: `rich_color_support`
- Python: `>=3.11,<4`
- Runtime dep: `rich >=13.0.0,<16.0.0`
- Build / deps: [Poetry](https://python-poetry.org/)
- Tests: `pytest`
- Formatters: `black`, `isort`

## Setup

```bash
poetry install
```

## Common commands

| Task | Command |
|---|---|
| Run tests | `poetry run pytest` |
| Format | `poetry run black . && poetry run isort .` |
| Build distribution | `poetry build` |
| Export requirements | `poetry export -f requirements.txt --output requirements.txt --without-hashes` |
| Run a script in env | `poetry run python -c "..."` |

A `Makefile` exists with shortcuts — read it before adding new ones.

## Code style

Within each Python file, keep this order:

1. Module docstring
2. Imports (stdlib → third-party → local; each block alphabetized via `isort`)
3. Module-level constants
4. Public functions
5. Public classes
6. Private functions / classes (prefixed with `_`)

Other conventions:

- Use **`black`** defaults for formatting; line length 88.
- Prefer `StrEnum` for color enums so values double as Rich-compatible color strings.
- Type-annotate all public APIs. Use `typing` imports compatible with Python 3.11+ (`list[X]`, `X | None` syntax is fine).
- Keep comments to the WHY, not the WHAT. Don't restate code.
- **Boy Scout Rule**: leave code cleaner than you found it — fix small issues (formatting, naming, dead code, missing types) in files you touch, but don't sprawl into unrelated refactors.

## Backwards compatibility

The library is pre-1.0 but treats public API as stable:

- All names re-exported from `rich_color_support/__init__.py` are public.
- Removing or renaming a public symbol requires a major-ish bump and a release note.
- Adding new symbols / modules is always fine.

## Testing

- Tests live in `tests/`; `conftest.py` provides a shared `rich.Console` fixture.
- Add a test for each new public function/class. Visual output tests can simply print using the new colors and assert they don't raise.
- Run the full suite before considering work done: `poetry run pytest`.

## Commit & PR style

- Commit messages on this repo use a leading sparkles emoji and a Conventional-Commits-ish prefix, e.g. `✨ feat(themes): add dark_theme()`. Follow that pattern.
- One logical change per commit. Don't bundle unrelated work.
- Reference issue numbers in the body if applicable.

## What NOT to do

- Don't introduce new runtime dependencies without discussion.
- Don't break the `RichColors* StrEnum` interface — third-party code may rely on the string values matching Rich's color names.
- Don't add CLI behavior outside `__main__.py` / `preview.py`.
- Don't commit generated files (`dist/`, `pip-log.txt` is legacy and may be removed).
