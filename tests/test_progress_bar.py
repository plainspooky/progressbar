"""
Tests for ProgressBar main module.
"""

from pytest import mark, raises

from progressbar import PADDING, ProgressBar
from progressbar.config import DEFAULT_COLUMN_WIDTH
from progressbar.console import VT100

HEX_TRIPLET_BLACK = "#000"
HEX_TRIPLET_WHITE = "#FFF"

RGB_TUPLE_BLACK = (0, 0, 0)
RGB_TUPLE_IKB = (0, 47, 167)
RGB_TUPLE_WHITE = (255, 255, 255)

PROGRESS_BAR_VALUE = 100
PROGRESS_PERCENT_VALUES = [
    ("0.0%", 0),
    ("25.0%", PROGRESS_BAR_VALUE * 0.25),
    ("50.0%", PROGRESS_BAR_VALUE * 0.50),
    ("75.0%", PROGRESS_BAR_VALUE * 0.75),
    ("100.0%", PROGRESS_BAR_VALUE),
]


class TestProgressBar:
    """Test ProgressBar class."""

    def test_class_instance(self):

        progress_bar = ProgressBar(PROGRESS_BAR_VALUE)

        assert isinstance(progress_bar, ProgressBar)
        assert progress_bar.width == DEFAULT_COLUMN_WIDTH - PADDING
        assert progress_bar.max_value == PROGRESS_BAR_VALUE
        assert progress_bar.bg is None
        assert progress_bar.fg is None

    def test_if_raises_exception_if_width_is_too_short(self):

        with raises(ValueError):
            is_too_short = PADDING
            ProgressBar(PROGRESS_BAR_VALUE, width=is_too_short)

    def test_if_keeps_right_foreground_and_background_given_colors(self):

        progress_bar = ProgressBar(
            PROGRESS_BAR_VALUE, fg=RGB_TUPLE_BLACK, bg=RGB_TUPLE_WHITE
        )

        assert (
            progress_bar.fg == RGB_TUPLE_BLACK
            and progress_bar.bg == RGB_TUPLE_WHITE
        )

    def test_if_removes_wrong_foreground_and_background_given_colors(self):

        progress_bar = ProgressBar(
            PROGRESS_BAR_VALUE, fg=HEX_TRIPLET_BLACK, bg=HEX_TRIPLET_WHITE
        )

        assert progress_bar.fg is None and progress_bar.bg is None

    def test_if_removes_only_the_wrong_background_color(self):

        progress_bar = ProgressBar(
            PROGRESS_BAR_VALUE, fg=RGB_TUPLE_WHITE, bg=HEX_TRIPLET_WHITE
        )

        assert progress_bar.fg is not None and progress_bar.bg is None

    def test_if_remove_only_the_wrong_foreground_color(self):

        progress_bar = ProgressBar(
            PROGRESS_BAR_VALUE, fg=HEX_TRIPLET_BLACK, bg=RGB_TUPLE_WHITE
        )

        assert progress_bar.fg is None and progress_bar.bg is not None

    @mark.parametrize("values", PROGRESS_PERCENT_VALUES)
    def test_if_progress_bar_is_rendered_with_correct_percentage_values(
        self, values
    ):

        progress_bar = ProgressBar(PROGRESS_BAR_VALUE)
        percent, size = values

        assert percent in progress_bar.view(size)

    def test_if_value_higher_than_max_value_is_ignored(self):

        progress_bar = ProgressBar(PROGRESS_BAR_VALUE)
        output = progress_bar.view(PROGRESS_BAR_VALUE)

        assert progress_bar.view(PROGRESS_BAR_VALUE + 1) == output

    def test_if_background_color_is_displayed_on_progress_bar(self):

        progress_bar = ProgressBar(PROGRESS_BAR_VALUE, bg=RGB_TUPLE_IKB)
        set_bg_color_code = VT100.set_bg_color.format(*RGB_TUPLE_IKB)

        assert set_bg_color_code in progress_bar.view(PROGRESS_BAR_VALUE)

    def test_if_foreground_color_is_displayed_on_progress_bar(self):

        progress_bar = ProgressBar(PROGRESS_BAR_VALUE, fg=RGB_TUPLE_IKB)
        set_fg_color_code = VT100.set_fg_color.format(*RGB_TUPLE_IKB)

        assert set_fg_color_code in progress_bar.view(PROGRESS_BAR_VALUE)

    def test_if_background_and_foreground_colors_are_displayed_on_progress_bar(
        self,
    ):

        progress_bar = ProgressBar(
            PROGRESS_BAR_VALUE, bg=RGB_TUPLE_WHITE, fg=RGB_TUPLE_IKB
        )
        assert VT100.reset_colors in progress_bar.view(PROGRESS_BAR_VALUE)
