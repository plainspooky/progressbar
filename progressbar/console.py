"""
Console helpers
"""
from .datatypes import ColorType
from devtools import debug


class VT100:
    """This just keeps some VT100 escape codes used to draw the progress
    bar on screen."""

    reset_colors = "\x1b[0m"
    restore_cursor = "\x1b[u"
    save_cursor = "\x1b[s"

    __color_codes = {
        "256": {
            "fg": "\x1b[38;5;{0}m",
            "bg": "\x1b[48;5;{0}m",
        },
        "truecolor": {
            "fg": "\x1b[38;2;{0};{1};{2}m",
            "bg": "\x1b[48;2;{0};{1};{2}m",
        },
    }

    def __set_color(color_attr: str, color: ColorType) -> str:

        if isinstance(color, int):
            mode, color_value = "256", (color,)
        elif isinstance(color, tuple):
            mode, color_value = "truecolor", color
        else:
            raise ValueError(f"invalid given color '{color}' has been used")

        return VT100.__color_codes[mode][color_attr].format(*color_value)

    def set_bg_color(color: ColorType) -> str:
        """Set background color for both indexed and truecolor values."""

        return VT100.__set_color("bg", color)

    def set_fg_color(color: ColorType) -> str:
        """Set foreground color for both indexed and truecolor values."""

        return VT100.__set_color("fg", color)
