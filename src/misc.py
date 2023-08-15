from enum import IntEnum, unique


@unique
class _ID(IntEnum):
    HUMAN = 1
    COMPUTER = 2


@unique
class Figure(IntEnum):
    """Enums for figures."""

    CROSS = _ID.HUMAN.value
    CIRCLE = _ID.COMPUTER.value


@unique
class PlayerID(IntEnum):
    """Enums for players (human or computer)."""

    HUMAN = _ID.HUMAN.value
    COMPUTER = _ID.COMPUTER.value
