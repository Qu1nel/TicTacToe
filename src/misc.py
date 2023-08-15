from enum import IntEnum, unique


@unique
class Figure(IntEnum):
    """Enums for figures."""

    CROSS = 2
    CIRCLE = 1
