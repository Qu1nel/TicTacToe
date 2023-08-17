from abc import abstractmethod

from src.game_state import GameState
from src.interface import Interface
from src.misc import PlayerID, SingletonABC


class AppBase(metaclass=SingletonABC):
    """Tic-Tac-Toe Application Abstract Class.

    Attributes:
        Interface: Window interface module.
        GameStates: Game state module.

    """

    Interface: Interface
    GameStates: GameState

    @abstractmethod
    def update(self, row: int, col: int, number_player: PlayerID) -> None:  # noqa: D102
        raise NotImplementedError

    @abstractmethod
    def restart(self) -> None:  # noqa: D102
        raise NotImplementedError

    @abstractmethod
    def check_win(self, player: int, draw: bool = True) -> bool:  # noqa: D102
        raise NotImplementedError
