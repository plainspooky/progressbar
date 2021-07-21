"""
Console helpers
"""


class VT100:
    """This just keeps some VT100 escape codes used to draw the progress
    bar on screen."""

    reset_colors = "\x1b[0m"
    restore_cursor = "\x1b[u"
    save_cursor = "\x1b[s"
    set_bg_color = "\x1b[48;2;{0};{1};{2}m"
    set_fg_color = "\x1b[38;2;{0};{1};{2}m"
