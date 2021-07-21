"""
Implements a smoothly progress bar on console using Unicode characters.

# Usage

There are some usage examples.

## Basic usage

Just try this:

``` python
from time import sleep
import progressbar as pb

bar = pb.ProgressBar(100)

for value in range(0, 101):
    print(bar.view(value), end="\\r")
    sleep(0.0125)

print("\\n")
```

The value of 100 means the maximum value accepted by progress bar. And it is
used to calculate the percentage as well.

## Custom width

By default progress bar is set to fit in 80 columns screen size but you can
resize it using:

``` python
from time import sleep
import progressbar as pb

bar = pb.ProgressBar(100, width=40)

for value in range(0, 101):
    print(bar.view(value), end="\\r")
    sleep(0.0125)

print("\\n")
```

It makes the progress bar fit in 40 characters.

## Setting colors

You can optionally set foreground and background colors for progress bar:

``` python
from time import sleep
import progressbar as pb

bar = pb.ProgressBar(100, bg=(63, 63, 63), fg=(255, 127, 0))

for value in range(0, 101):
    print(bar.view(value), end="\\r")
    sleep(0.0125)

print("\\n")
```

This example set dark grey for background and orange for foreground (the bar
iself).

Colors are defined using a tuple containing («red», «green», «blue») value
sand you can change colors any time:

``` python
from time import sleep
import progressbar as pb

red = 0
bar = pb.ProgressBar(255, bg=(0, 31, 63), fg=(red, 0, 0))

for value in range(0, 256):
    print(bar.view(value), end="\\r")
    red += 1
    sleep(0.0125)
    bar.fg = (red, 0, 0)

print("\\n")
```

This example changes foreground color at each `for` iteration.

## Changing bar style

You can also use another set of characters to draw the progress bar:

``` python
from time import sleep
import progressbar as pb

bar = pb.ProgressBar(127, blocks=" ░▒▓█")

for value in range(0, 127 + 1):
    print(bar.view(value), end="\\r")
    sleep(0.125)

print("\\n")

```

The first character is used to draw the empty space, and the others are used
to draw the grades of progress bar.

---

In "helpers" there are some function that can be usefull to retrieve screen
width and to handle with colors.
"""
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

        self.bg = sanitize_color(self.bg)
        self.fg = sanitize_color(self.fg)

    def __create_progress_bar(self, value: int) -> str:

        full = int(value // self.__steps)
        partial = int(value % self.__steps)

        result = ""

        if self.fg:
            result += VT100.set_fg_color.format(*self.fg)

        if self.bg:
            result += VT100.set_bg_color.format(*self.bg)

        result += (
            self.blocks[-1] * full + (self.blocks[partial] if partial else "")
        ).ljust(self.width, self.blocks[0])

        if self.fg or self.bg:
            result += VT100.reset_colors

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

        return (
            f"{VT100.save_cursor} {bar} {percent: .1%} {VT100.restore_cursor}"
        )
