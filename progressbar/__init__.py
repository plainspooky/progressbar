"""
Implements a smoothly progress bar to be used on console and XTerm that uses
Unicode characters and VT100 colors.

# Installation

To install the lastest version, use:

``` shell
pip install git+https://github.com/plainspooky/progressbar
```

# Usage

## Basic usage

To create a simple progress bar, try this:

``` python
from time import sleep

import progressbar as pb

bar = pb.ProgressBar(100)

for value in range(0, 101):
    print(bar.view(value), end="\\r")
    sleep(0.0125)

print("\\n")
```

The value of 100 is the maximum value accepted by the progress bar and is
used to calculate the percentage as well.

## Custom width

By default the progress bar is fits to 80 columns screen size but you can set
progress bar witdh using:

``` python
from time import sleep

import progressbar as pb

bar = pb.ProgressBar(100, width=40)

for value in range(0, 101):
    print(bar.view(value), end="\\r")
    sleep(0.0125)

print("\\n")
```

You can also use `.resize(«new value»)` to change bar width at anytime.

## Setting colors

Custom background and foregound colors can be used
BYou can optionally set foreground and background colors for the progress bar.


``` python
from time import sleep

import progressbar as pb

bar = pb.ProgressBar(100, bg=(63, 63, 63), fg=(255, 127, 0))

for value in range(0, 101):
    print(bar.view(value), end="\\r")
    sleep(0.0125)

print("\\n")
```

This example set the progress bar to use dark grey as background and orange
as foreground.

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
from .core import ProgressBar, PADDING
