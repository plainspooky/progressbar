"""
Tests for helpers functions.
"""
from unittest import mock

from pytest import mark, raises

from progressbar.config import DEFAULT_COLUMN_WIDTH
from progressbar.helpers import (
    MAX_RGB_VALUE,
    MIN_RGB_VALUE,
    convert_hex_colors,
    get_random_color,
    get_width_by_environment,
    get_width_from_os,
    sanitize_color,
)

CUSTOM_COLUMNS_VALUE = DEFAULT_COLUMN_WIDTH

ILLEGAL_HEX_TRIPLETS = ("", "#", "000", "#12", "#1234", "#12345", "#1234567")

UNSANITIZED_COLORS = (
    (MIN_RGB_VALUE),
    (MIN_RGB_VALUE, MAX_RGB_VALUE),
    (MIN_RGB_VALUE, MAX_RGB_VALUE, MIN_RGB_VALUE, MAX_RGB_VALUE),
    (MIN_RGB_VALUE, MIN_RGB_VALUE, MIN_RGB_VALUE),
    (MAX_RGB_VALUE, MAX_RGB_VALUE, MAX_RGB_VALUE),
    (MIN_RGB_VALUE - 1, MIN_RGB_VALUE - 1, MIN_RGB_VALUE - 1),
    (MAX_RGB_VALUE + 1, MAX_RGB_VALUE + 1, MAX_RGB_VALUE + 1),
)

SANITIZED_COLORS = (
    None,
    None,
    None,
    (MIN_RGB_VALUE, MIN_RGB_VALUE, MIN_RGB_VALUE),
    (MAX_RGB_VALUE, MAX_RGB_VALUE, MAX_RGB_VALUE),
    (MIN_RGB_VALUE, MIN_RGB_VALUE, MIN_RGB_VALUE),
    (MAX_RGB_VALUE, MAX_RGB_VALUE, MAX_RGB_VALUE),
)

COLOR_SAMPLES = zip(UNSANITIZED_COLORS, SANITIZED_COLORS)


@mark.parametrize("color", ILLEGAL_HEX_TRIPLETS)
def test_if_raises_exception_when_using_invalid_hex_triplets(color) -> None:

    with raises(ValueError):
        convert_hex_colors(color)


def test_if_converts_3_digit_hex_triplet_to_rgb_tuple() -> None:

    color = "#123"
    assert convert_hex_colors(color) == (17, 34, 51)


def test_if_converts_6_digit_hex_triplet_to_rgb_tuple() -> None:

    color = "#012345"
    assert convert_hex_colors(color) == (1, 35, 69)


@mock.patch.dict("os.environ", {"COLUMNS": str(CUSTOM_COLUMNS_VALUE)})
def test_if_get_screen_width_by_environment_variable() -> None:

    assert get_width_by_environment() == CUSTOM_COLUMNS_VALUE


@mock.patch.dict("os.environ", {"COLUMNS": ""})
def test_if_raises_an_exception_if_environ_variabled_doesnt_exist() -> None:

    with raises(ValueError):
        get_width_by_environment()


def test_if_get_screen_width_directly_from_operating_system() -> None:

    with mock.patch(
        "progressbar.helpers.__get_width_on_posix",
        return_value=CUSTOM_COLUMNS_VALUE,
    ):
        assert get_width_from_os() == CUSTOM_COLUMNS_VALUE


def test_if_get_valid_values_for_get_random_colors() -> None:

    for value in get_random_color():
        assert value >= MIN_RGB_VALUE and value <= MAX_RGB_VALUE


@mark.parametrize("color", COLOR_SAMPLES)
def test_with_sanitize_colors_discards_illegal_values(color) -> None:
    given, expected = color
    assert sanitize_color(given) == expected
