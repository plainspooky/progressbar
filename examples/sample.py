#!/usr/bin/env python3
from random import randint
from time import sleep

from progressbar import ProgressBar
from progressbar.helpers import (
    get_random_color,
    get_width_by_environment,
    get_width_from_os,
)

if __name__ == "__main__":

    while True:
        try:
            cols = get_width_by_environment()
        except ValueError:
            cols = get_width_from_os()

        value = randint(10, 1000)
        fore = get_random_color()
        back = tuple([255 - i for i in fore])

        progress_bar = ProgressBar(
            max_value=value, width=cols, fg=fore, bg=back
        )

        for i in range(0, value + 1):
            print(progress_bar.view(i), end="\r")
            sleep(0.0125)

        print("\n")
