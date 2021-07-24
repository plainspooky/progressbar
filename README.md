progressbar
---

Implements a smoothly progress bar on console using Unicode characters.

# Installation

Use

``` shell
pip install git+https://github.com/plainspooky/progressbar
```

To install the lastest version.

# Usage

There are some usage examples.

## Basic usage

Just try this:

``` python
from time import sleep
import progressbar as pb

bar = pb.ProgressBar(100)

for value in range(0, 101):
    print(bar.view(value), end="\r")
    sleep(0.0125)

print("\n")
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
    print(bar.view(value), end="\r")
    sleep(0.0125)

print("\n")
```

It makes the progress bar fit in 40 characters.

## Setting colors

You can optionally set foreground and background colors for progress bar:

``` python
from time import sleep
import progressbar as pb

bar = pb.ProgressBar(100, bg=(63, 63, 63), fg=(255, 127, 0))

for value in range(0, 101):
    print(bar.view(value), end="\r")
    sleep(0.0125)

print("\n")
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
    print(bar.view(value), end="\r")
    red += 1
    sleep(0.0125)
    bar.fg = (red, 0, 0)

print("\n")
```

This example changes foreground color at each `for` iteration.

## Changing bar style

You can also use another set of characters to draw the progress bar:

``` python
from time import sleep
import progressbar as pb

bar = pb.ProgressBar(127, blocks=" ░▒▓█")

for value in range(0, 127 + 1):
    print(bar.view(value), end="\r")
    sleep(0.125)

print("\n")

```

The first character is used to draw the empty space, and the others are used
to draw the grades of progress bar.

---

In "helpers" there are some function that can be usefull to retrieve screen
width and to handle with colors.
