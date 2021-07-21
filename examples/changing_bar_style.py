#!/usr/bin/env python3
from time import sleep

import progressbar as pb

bar = pb.ProgressBar(127, blocks=" ░▒▓█")

for value in range(0, 127 + 1):
    print(bar.view(value), end="\r")
    sleep(0.125)

print("\n")
