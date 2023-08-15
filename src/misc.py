from enum import IntEnum, unique


@unique
class Figure(IntEnum):
    """Enums for figures."""

    CROSS = 2
    CIRCLE = 1


@unique
class PlayerID(IntEnum):
    """Enums for players (human or computer)."""

    HUMAN = 1
    COMPUTER = 2
