#!/usr/bin/env python3
import progressbar

if __name__ == "__main__":
    with open("README.md", "w") as f:
        f.write(progressbar.__name__ + "\n---\n")
        f.write(progressbar.__doc__)
