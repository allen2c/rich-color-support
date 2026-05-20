"""Filter color palettes by hue, brightness, temperature, and saturation."""

from typing import Iterable, Literal, NamedTuple, get_args

from rich_color_support._palettes import RichColors, RichColorsBase

HueLiteral = Literal[
    "red",
    "orange",
    "yellow",
    "green",
    "cyan",
    "blue",
    "purple",
    "pink",
    "neutral",
]
BrightnessLiteral = Literal["light", "mid", "dark"]
TemperatureLiteral = Literal["warm", "cool", "neutral"]
SaturationLiteral = Literal["vivid", "muted"]

_HUES = frozenset(get_args(HueLiteral))
_BRIGHTNESSES = frozenset(get_args(BrightnessLiteral))
_TEMPERATURES = frozenset(get_args(TemperatureLiteral))
_SATURATIONS = frozenset(get_args(SaturationLiteral))


class _ColorAttrs(NamedTuple):
    """Classification row for a single color: hue, brightness, temperature, saturation."""

    hue: str
    brightness: str
    temperature: str
    saturation: str


# Classification table for every RichColors member.
# Initial values generated via HSL math, then hand-reviewed against
# colloquial color-naming conventions (e.g. chartreuse is green-warm,
# plum is purple, misty rose is pink).
_CLASSIFICATION: dict[str, _ColorAttrs] = {
    "navy_blue": _ColorAttrs("blue", "dark", "cool", "vivid"),
    "dark_blue": _ColorAttrs("blue", "dark", "cool", "vivid"),
    "blue3": _ColorAttrs("blue", "mid", "cool", "vivid"),
    "blue1": _ColorAttrs("blue", "mid", "cool", "vivid"),
    "dark_green": _ColorAttrs("green", "dark", "cool", "vivid"),
    "deep_sky_blue4": _ColorAttrs("blue", "mid", "cool", "vivid"),
    "dodger_blue3": _ColorAttrs("blue", "mid", "cool", "vivid"),
    "dodger_blue2": _ColorAttrs("blue", "mid", "cool", "vivid"),
    "green4": _ColorAttrs("green", "dark", "cool", "vivid"),
    "spring_green4": _ColorAttrs("green", "dark", "cool", "vivid"),
    "turquoise4": _ColorAttrs("cyan", "dark", "cool", "vivid"),
    "deep_sky_blue3": _ColorAttrs("blue", "mid", "cool", "vivid"),
    "dodger_blue1": _ColorAttrs("blue", "mid", "cool", "vivid"),
    "dark_cyan": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "light_sea_green": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "deep_sky_blue2": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "deep_sky_blue1": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "green3": _ColorAttrs("green", "mid", "cool", "vivid"),
    "spring_green3": _ColorAttrs("green", "mid", "cool", "vivid"),
    "cyan3": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "dark_turquoise": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "turquoise2": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "green1": _ColorAttrs("green", "mid", "cool", "vivid"),
    "spring_green2": _ColorAttrs("green", "mid", "cool", "vivid"),
    "spring_green1": _ColorAttrs("green", "mid", "cool", "vivid"),
    "medium_spring_green": _ColorAttrs("green", "mid", "cool", "vivid"),
    "cyan2": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "cyan1": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "purple4": _ColorAttrs("purple", "dark", "cool", "vivid"),
    "purple3": _ColorAttrs("purple", "mid", "cool", "vivid"),
    "blue_violet": _ColorAttrs("purple", "mid", "cool", "vivid"),
    "medium_purple4": _ColorAttrs("purple", "mid", "cool", "muted"),
    "slate_blue3": _ColorAttrs("blue", "mid", "cool", "vivid"),
    "royal_blue1": _ColorAttrs("blue", "light", "cool", "vivid"),
    "chartreuse4": _ColorAttrs("green", "dark", "warm", "vivid"),
    "pale_turquoise4": _ColorAttrs("cyan", "mid", "cool", "muted"),
    "steel_blue": _ColorAttrs("blue", "mid", "cool", "muted"),
    "steel_blue3": _ColorAttrs("blue", "mid", "cool", "vivid"),
    "cornflower_blue": _ColorAttrs("blue", "light", "cool", "vivid"),
    "dark_sea_green4": _ColorAttrs("green", "mid", "cool", "muted"),
    "cadet_blue": _ColorAttrs("cyan", "mid", "cool", "muted"),
    "sky_blue3": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "chartreuse3": _ColorAttrs("green", "mid", "warm", "vivid"),
    "sea_green3": _ColorAttrs("green", "mid", "cool", "vivid"),
    "aquamarine3": _ColorAttrs("green", "mid", "cool", "vivid"),
    "medium_turquoise": _ColorAttrs("cyan", "mid", "cool", "vivid"),
    "steel_blue1": _ColorAttrs("cyan", "light", "cool", "vivid"),
    "sea_green2": _ColorAttrs("green", "light", "cool", "vivid"),
    "sea_green1": _ColorAttrs("green", "light", "cool", "vivid"),
    "dark_slate_gray2": _ColorAttrs("cyan", "light", "cool", "vivid"),
    "dark_red": _ColorAttrs("red", "dark", "warm", "vivid"),
    "dark_magenta": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "orange4": _ColorAttrs("orange", "dark", "warm", "vivid"),
    "light_pink4": _ColorAttrs("pink", "mid", "warm", "muted"),
    "plum4": _ColorAttrs("purple", "mid", "cool", "muted"),
    "medium_purple3": _ColorAttrs("purple", "mid", "cool", "vivid"),
    "slate_blue1": _ColorAttrs("purple", "light", "cool", "vivid"),
    "wheat4": _ColorAttrs("yellow", "mid", "warm", "muted"),
    "light_slate_grey": _ColorAttrs("neutral", "mid", "neutral", "muted"),
    "medium_purple": _ColorAttrs("purple", "light", "cool", "muted"),
    "light_slate_blue": _ColorAttrs("blue", "light", "cool", "vivid"),
    "yellow4": _ColorAttrs("yellow", "mid", "warm", "vivid"),
    "dark_sea_green": _ColorAttrs("green", "mid", "cool", "muted"),
    "light_sky_blue3": _ColorAttrs("blue", "light", "cool", "muted"),
    "sky_blue2": _ColorAttrs("blue", "light", "cool", "vivid"),
    "chartreuse2": _ColorAttrs("green", "mid", "warm", "vivid"),
    "pale_green3": _ColorAttrs("green", "light", "cool", "muted"),
    "dark_slate_gray3": _ColorAttrs("cyan", "light", "cool", "muted"),
    "sky_blue1": _ColorAttrs("cyan", "light", "cool", "vivid"),
    "chartreuse1": _ColorAttrs("green", "mid", "warm", "vivid"),
    "light_green": _ColorAttrs("green", "light", "cool", "vivid"),
    "aquamarine1": _ColorAttrs("green", "light", "cool", "vivid"),
    "dark_slate_gray1": _ColorAttrs("cyan", "light", "cool", "vivid"),
    "deep_pink4": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "medium_violet_red": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "dark_violet": _ColorAttrs("purple", "mid", "cool", "vivid"),
    "purple": _ColorAttrs("purple", "mid", "cool", "vivid"),
    "medium_orchid3": _ColorAttrs("purple", "mid", "cool", "muted"),
    "medium_orchid": _ColorAttrs("purple", "mid", "cool", "vivid"),
    "dark_goldenrod": _ColorAttrs("yellow", "mid", "warm", "vivid"),
    "rosy_brown": _ColorAttrs("red", "mid", "warm", "muted"),
    "medium_purple2": _ColorAttrs("purple", "light", "cool", "muted"),
    "medium_purple1": _ColorAttrs("purple", "light", "cool", "vivid"),
    "dark_khaki": _ColorAttrs("yellow", "mid", "warm", "muted"),
    "navajo_white3": _ColorAttrs("orange", "mid", "warm", "muted"),
    "light_steel_blue3": _ColorAttrs("blue", "light", "cool", "muted"),
    "light_steel_blue": _ColorAttrs("blue", "light", "cool", "vivid"),
    "dark_olive_green3": _ColorAttrs("green", "mid", "warm", "vivid"),
    "dark_sea_green3": _ColorAttrs("green", "light", "cool", "muted"),
    "light_cyan3": _ColorAttrs("cyan", "light", "cool", "muted"),
    "light_sky_blue1": _ColorAttrs("blue", "light", "cool", "vivid"),
    "green_yellow": _ColorAttrs("green", "mid", "warm", "vivid"),
    "dark_olive_green2": _ColorAttrs("green", "light", "warm", "vivid"),
    "pale_green1": _ColorAttrs("green", "light", "cool", "vivid"),
    "dark_sea_green2": _ColorAttrs("green", "light", "cool", "vivid"),
    "pale_turquoise1": _ColorAttrs("cyan", "light", "cool", "vivid"),
    "red3": _ColorAttrs("red", "mid", "warm", "vivid"),
    "deep_pink3": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "magenta3": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "dark_orange3": _ColorAttrs("orange", "mid", "warm", "vivid"),
    "indian_red": _ColorAttrs("red", "mid", "warm", "vivid"),
    "hot_pink3": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "hot_pink2": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "orchid": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "orange3": _ColorAttrs("orange", "mid", "warm", "vivid"),
    "light_salmon3": _ColorAttrs("orange", "mid", "warm", "vivid"),
    "light_pink3": _ColorAttrs("pink", "light", "warm", "muted"),
    "pink3": _ColorAttrs("pink", "light", "warm", "muted"),
    "plum3": _ColorAttrs("purple", "light", "cool", "muted"),
    "violet": _ColorAttrs("purple", "light", "cool", "vivid"),
    "gold3": _ColorAttrs("yellow", "mid", "warm", "vivid"),
    "light_goldenrod3": _ColorAttrs("yellow", "mid", "warm", "vivid"),
    "tan": _ColorAttrs("orange", "light", "warm", "muted"),
    "misty_rose3": _ColorAttrs("pink", "light", "warm", "muted"),
    "thistle3": _ColorAttrs("pink", "light", "warm", "muted"),
    "plum2": _ColorAttrs("purple", "light", "cool", "vivid"),
    "yellow3": _ColorAttrs("yellow", "mid", "warm", "vivid"),
    "khaki3": _ColorAttrs("yellow", "mid", "warm", "vivid"),
    "light_yellow3": _ColorAttrs("yellow", "light", "warm", "muted"),
    "light_steel_blue1": _ColorAttrs("blue", "light", "cool", "vivid"),
    "yellow2": _ColorAttrs("yellow", "mid", "warm", "vivid"),
    "dark_olive_green1": _ColorAttrs("green", "light", "warm", "vivid"),
    "dark_sea_green1": _ColorAttrs("green", "light", "cool", "vivid"),
    "honeydew2": _ColorAttrs("neutral", "light", "neutral", "muted"),
    "light_cyan1": _ColorAttrs("cyan", "light", "cool", "vivid"),
    "red1": _ColorAttrs("red", "mid", "warm", "vivid"),
    "deep_pink2": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "deep_pink1": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "magenta2": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "magenta1": _ColorAttrs("pink", "mid", "warm", "vivid"),
    "orange_red1": _ColorAttrs("orange", "mid", "warm", "vivid"),
    "indian_red1": _ColorAttrs("red", "light", "warm", "vivid"),
    "hot_pink": _ColorAttrs("pink", "light", "warm", "vivid"),
    "medium_orchid1": _ColorAttrs("purple", "light", "cool", "vivid"),
    "dark_orange": _ColorAttrs("orange", "mid", "warm", "vivid"),
    "salmon1": _ColorAttrs("orange", "light", "warm", "vivid"),
    "light_coral": _ColorAttrs("red", "light", "warm", "vivid"),
    "pale_violet_red1": _ColorAttrs("pink", "light", "warm", "vivid"),
    "orchid2": _ColorAttrs("pink", "light", "warm", "vivid"),
    "orchid1": _ColorAttrs("pink", "light", "warm", "vivid"),
    "orange1": _ColorAttrs("orange", "mid", "warm", "vivid"),
    "sandy_brown": _ColorAttrs("orange", "light", "warm", "vivid"),
    "light_salmon1": _ColorAttrs("orange", "light", "warm", "vivid"),
    "light_pink1": _ColorAttrs("pink", "light", "warm", "vivid"),
    "pink1": _ColorAttrs("pink", "light", "warm", "vivid"),
    "plum1": _ColorAttrs("purple", "light", "cool", "vivid"),
    "gold1": _ColorAttrs("yellow", "mid", "warm", "vivid"),
    "light_goldenrod2": _ColorAttrs("yellow", "light", "warm", "vivid"),
    "navajo_white1": _ColorAttrs("orange", "light", "warm", "vivid"),
    "misty_rose1": _ColorAttrs("pink", "light", "warm", "vivid"),
    "thistle1": _ColorAttrs("pink", "light", "warm", "vivid"),
    "yellow1": _ColorAttrs("yellow", "mid", "warm", "vivid"),
    "light_goldenrod1": _ColorAttrs("yellow", "light", "warm", "vivid"),
    "khaki1": _ColorAttrs("yellow", "light", "warm", "vivid"),
    "wheat1": _ColorAttrs("yellow", "light", "warm", "vivid"),
    "cornsilk1": _ColorAttrs("yellow", "light", "warm", "vivid"),
}


def filter_colors(
    palette: type[RichColorsBase] | Iterable[RichColorsBase] = RichColors,
    *,
    hue: HueLiteral | None = None,
    brightness: BrightnessLiteral | None = None,
    temperature: TemperatureLiteral | None = None,
    saturation: SaturationLiteral | None = None,
) -> list[RichColorsBase]:
    """Return palette members matching all given criteria (AND-combined).

    Members not present in the classification table (e.g. plain "white"
    from RichColors8) are silently excluded from the result.
    """
    _validate("hue", hue, _HUES)
    _validate("brightness", brightness, _BRIGHTNESSES)
    _validate("temperature", temperature, _TEMPERATURES)
    _validate("saturation", saturation, _SATURATIONS)

    result: list[RichColorsBase] = []
    for member in list(palette):
        attrs = _CLASSIFICATION.get(member.value)
        if attrs is None:
            continue
        if hue is not None and attrs.hue != hue:
            continue
        if brightness is not None and attrs.brightness != brightness:
            continue
        if temperature is not None and attrs.temperature != temperature:
            continue
        if saturation is not None and attrs.saturation != saturation:
            continue
        result.append(member)
    return result


def _validate(name: str, value: str | None, allowed: frozenset[str]) -> None:
    if value is None:
        return
    if value not in allowed:
        raise ValueError(f"Invalid {name}={value!r}; expected one of {sorted(allowed)}")
