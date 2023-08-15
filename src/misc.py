from enum import IntEnum, unique
from typing import Any, ClassVar


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


class Singleton(type):
    """Class template singleton."""

    _instances: ClassVar[dict] = {}

    def __call__(cls: Any, *args: Any, **kwargs: Any):  # type: ignore  # noqa: ANN204, D102
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
