#!/usr/bin/env python3
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
