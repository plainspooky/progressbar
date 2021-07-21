"""
Tests for console module.
"""
from pytest import mark

from progressbar.console import VT100

ALL_CODES = [i for i in dir(VT100) if i[0:2] != "__"]
COLOR_CODES = ["set_bg_color", "set_fg_color"]


class TestVT100:
    """Test VT100 attributes."""

    @mark.parametrize("code", ALL_CODES)
    def test_if_all_escape_codes_contains_a_esc_character(self, code) -> None:

        assert getattr(VT100, code)[0] == "\x1b"

    @mark.parametrize("code", COLOR_CODES)
    def test_if_color_codes_contains_replacement_fields(self, code) -> None:

        color_code = getattr(VT100, code)

        assert "{0}" in color_code
        assert "{1}" in color_code
        assert "{2}" in color_code
        assert "{3}" not in color_code
