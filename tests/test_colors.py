"""
Tests for console module.
"""
from pytest import fixture

from progressbar import colors


@fixture
def all_colors() -> set:
    return set(
        [color_name for color_name in dir(colors) if color_name[0] != "_"]
    )


class TestColors:
    """Test color values"""

    def test_if_there_are_exactly_256_colors_defined(self, all_colors) -> None:
        assert len(all_colors) == 256

    def teest_if_color_values_are_all_integers_between_0_and_255(
        self, all_colors
    ) -> None:
        for color in all_colors:
            assert isinstance(color, int)
            assert color >= 0 and color <= 255
