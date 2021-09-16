"""
Tests for console module.
"""
from pytest import mark

from progressbar.console import VT100

ALL_CODES = ["reset_colors", "restore_cursor", "save_cursor"]

# COLOR_CODES = ["set_bg_color", "set_fg_color"]


class TestVT100:
    """Test VT100 attributes."""

    @mark.parametrize("code", ALL_CODES)
    def test_if_all_escape_codes_contains_an_esc_character(self, code) -> None:

        assert getattr(VT100, code)[0] == "\x1b"

    def test_set_of_indexed_color_to_fg_and_bg_colors(self) -> None:
        color = VT100.set_bg_color(0)
        color = VT100.set_fg_color(0)

    # @mark.parametrize("code", COLOR_CODES)
    # def test_if_color_codes_contains_replacement_fields(self, code) -> None:
    #
    #     color_code = getattr(VT100, code)
    #
    #     assert "{0}" in color_code
    #     assert "{1}" in color_code
    #     assert "{2}" in color_code
    #     assert "{3}" not in color_code
