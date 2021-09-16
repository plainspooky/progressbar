from progressbar import colors
from progressbar.console import VT100

BLOCK = "\u2588\u258C"

all_colors = [
    (color_name, getattr(colors, color_name))
    for color_name in dir(colors)
    if color_name[0] != "_"
]
all_colors.sort(key=lambda i: i[1])

column = len(max(all_colors, key=lambda i: len(i[0]))[0]) + 1
fmt_string = "{3}{0}{1}{2:<" + str(column) + "}"

color_name_and_escape = (
    (color[0], VT100.set_fg_color(color[1])) for color in all_colors
)

# print all 256 colors on a 4 columns x 64 lines table
for row in range(64):
    for col in range(4):
        print(
            fmt_string.format(
                BLOCK, VT100.reset_colors, *next(color_name_and_escape)
            ),
            end="",
        )
    print()
