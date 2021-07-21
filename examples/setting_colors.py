#!/usr/bin/env python3
from time import sleep

import progressbar as pb

bar = pb.ProgressBar(100, bg=(63, 63, 63), fg=(255, 127, 0))

for value in range(0, 101):
    print(bar.view(value), end="\r")
    sleep(0.0125)

print("\n")
