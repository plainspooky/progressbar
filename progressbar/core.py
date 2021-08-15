# progressbar
# https://github.com/plainspooky/progressbar
#
# Implements a smoothly progress bar on console and XTerm using Unicode
# characters and VT100 colors.
#
# Copyright (C) 2021  Giovanni Nunes
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from dataclasses import dataclass

from .config import DEFAULT_BLOCKS, DEFAULT_COLUMN_WIDTH
from .console import VT100
from .datatypes import ColorType
from .helpers import sanitize_color

PADDING = 9


@dataclass
class ProgressBar:
    """Manages a progress bar on console."""

    min_value = 0

    max_value: float
    width: int = DEFAULT_COLUMN_WIDTH
    fg: ColorType = None
    bg: ColorType = None
    blocks: str = DEFAULT_BLOCKS

    def __post_init__(self) -> None:

        self.__steps = len(self.blocks)
        self.resize(self.width)

        self.__t = VT100

        self.bg = sanitize_color(self.bg)
        self.fg = sanitize_color(self.fg)

    def __create_progress_bar(self, value: int) -> str:

        full = int(value // self.__steps)
        partial = int(value % self.__steps)

        result = ""

        if self.fg:
            result += self.__t.set_fg_color(self.fg)

        if self.bg:
            result += self.__t.set_bg_color(self.bg)

        result += (
            self.blocks[-1] * full + (self.blocks[partial] if partial else "")
        ).ljust(self.width, self.blocks[0])

        if self.fg or self.bg:
            result += self.__t.reset_colors

        return result

    def resize(self, new_width: int = 0) -> None:
        """Forces a new width for progress bar."""

        if new_width < PADDING + 1:
            raise ValueError("Bar width is too short!")

        self.width = new_width - PADDING

    def view(self, value: float) -> str:
        """View progress bar by a given value."""

        if value > self.max_value:
            value = self.max_value

        percent = float(value / self.max_value)

        bar = self.__create_progress_bar(
            value * (self.width * self.__steps) / self.max_value
        )

        return f"{self.__t.save_cursor} {bar} {percent: .1%} {self.__t.restore_cursor}"
