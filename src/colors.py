from dataclasses import astuple, dataclass
from enum import Enum, unique

from src.misc import not_valid_color_channels

BG_COLOR = (155, 89, 182)
BG_LINE_COLOR = (142, 68, 173)
CIRCLE_COLOR = (149, 165, 166)
CROSS_COLOR = (66, 66, 66)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)


@dataclass(slots=True)
class RGBA:
    """Simple RGBA model color.

    Attributes:
        R: Red color channel
        G: Green color channel
        B: Blue color channel
        A: Alpha transparent channel


    Methods:
        to_hex(self, alpha, /) -> str:
        to_rgb(self, alpha, /) -> tuple:

    """

    R: int
    G: int
    B: int
    A: int

    def __init__(self, r: int = 0, g: int = 0, b: int = 0, a: int = 255) -> None:
        if channel := not_valid_color_channels(r, g, b, a):
            msg = f"The color channel value must be between 0 and 255, but not {channel}"
            raise ValueError(msg)

        self.R, self.G, self.B, self.A = r, g, b, a

    def to_hex(self, alpha: bool = False) -> str:
        """String representation of color in hex format.

        Args:
            alpha: If True, then the alpha channel is taken into account.

        Returns:
            String representation of color in hex format.

        """
        rgb_hex = f"#{self.R:02X}{self.G:02X}{self.B:02X}"

        return f"{rgb_hex}{self.A:02X}" if alpha is True else rgb_hex

    def to_rgb(self, alpha: bool = False) -> tuple:
        """Tuple representation of color in rgb(a) format.

        Args:
            alpha: If True, then the alpha channel is taken into account.

        Returns:
            Tuple of integers representation of color in rgb(a) format.

        """
        return astuple(self) if alpha is True else astuple(self)[:-1]


@unique
class Color(Enum):
    """Enums for colors."""

    RED = RGBA(r=255, g=0, b=0)
    GREEN = RGBA(r=0, g=255, b=0)
    BLUE = RGBA(r=0, g=0, b=255)

    GRAY = RGBA(r=128, g=128, b=128)
    WHITE = RGBA(r=255, g=255, b=255)
    BLACK = RGBA(r=0, g=0, b=0)

    BG = RGBA(r=34, g=34, b=34)
    BG_LINE = RGBA(r=255, g=255, b=0)

    def __str__(self) -> str:  # noqa: D105
        return self.name.lower()

    def hex(self, alpha: bool = False) -> str:  # noqa: A003
        """String representation of color in hex format.

        Args:
            alpha: If True, then the alpha channel is taken into account.

        Returns:
            String representation of color in hex format.

        """
        return self.value.to_hex(alpha)

    def rgb(self, alpha: bool = False) -> tuple[int, ...]:
        """Tuple representation of color in rgb'a format.

        Args:
            alpha: If True, then the alpha channel is taken into account.

        Returns:
            Tuple of integers representation of color in rgb(a) format.

        """
        return self.value.to_rgb(alpha)


def get_rgb_color(color: RGBA | Color) -> tuple[int, ...]:
    """Checks the color for rgb and to_rgb methods, returns the rgb color.

    Args:
        color: RGBA or Color instance.


    Returns:
        Correct tuple[r, g, b] view color.

    Raises:
        TypeError: If color is not Color or RGBA class.

    """
    if isinstance(color, Color):
        rgb = color.rgb()
    elif isinstance(color, RGBA):
        rgb = color.to_rgb()
    else:
        msg = f"object BackGround must be {RGBA} or {Color} class. but not {type(color)}."
        raise TypeError(msg)

    return rgb
