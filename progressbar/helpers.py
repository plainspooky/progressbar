"""
Functions that help to work on console terminal.
"""
from os import environ, name, popen
from random import randint

from .config import DEFAULT_COLUMN_WIDTH, MAX_RGB_VALUE, MIN_RGB_VALUE, POSIX
from .datatypes import ColorType


def convert_hex_colors(color: str) -> ColorType:
    """Converts hexadecimal formated colors to a tuple with RGB values.

    Connversion from 3-bit to 6-bit is made by repeating each color component,
    e.g., `#123` is translated as `#112233`.

    source [Wikipedia](https://en.wikipedia.org/wiki/Web_colors#Shorthand_hexadecimal_form)"""  # noqa E501

    if len(color) and color[0] == "#" and len(color) in (4, 7):

        position, size, step = (2, 3, 1) if len(color) == 4 else (3, 6, 2)

        r, g, b = [
            int(color[i + 1 : i + position], 16)  # noqa E203
            for i in range(0, size, step)
        ]

        if len(color) == 4:
            r += r * 16
            g += g * 16
            b += b * 16

        return (r, g, b)

    raise ValueError(f"Invalid hexadecimal triplet '{color}'")


def get_random_color() -> ColorType:
    """Generates a random RGB color as a tuple of values."""

    return tuple([randint(MIN_RGB_VALUE, MAX_RGB_VALUE) for __ in range(3)])


def get_width_from_os() -> int:
    """Get terminal width using operating system tools (POSIX only)."""

    cols = {
        POSIX: __get_width_on_posix(),
    }.get(name)

    return int(cols) if cols else DEFAULT_COLUMN_WIDTH


def __get_width_on_posix() -> str:
    """Get terminal width on POSIX systems."""

    command = popen("stty size", "r")
    __, cols = command.read().split()

    return cols


def get_width_by_environment() -> int:
    """Get terminal width by environment variable."""

    if cols := environ.get("COLUMNS", DEFAULT_COLUMN_WIDTH):
        return int(cols)

    raise ValueError(
        "Environment variable 'COLUMNS' does not exist or is empty!"
    )


def sanitize_color(color: ColorType) -> ColorType:
    """A valid color is a tuple with 3 elements and any different number of
    elements will return None. Values have to be between 0 and 255 and are
    croped. (see MAX_RGB_VALUE and MIN_RGB_VALUE.)"""

    if color:
        return (
            None
            if len(color) != 3
            else tuple(
                [
                    MIN_RGB_VALUE
                    if i < MIN_RGB_VALUE
                    else MAX_RGB_VALUE
                    if i > MAX_RGB_VALUE
                    else i
                    for i in color
                ]
            )
        )
