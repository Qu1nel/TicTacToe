from typing import Optional

from src.config import FIRST_MOVE
from src.misc import PlayerID, SingletonABC


class GameState(metaclass=SingletonABC):
    """Game state class.

    Attributes:
        game_over: A flag indicating that the end of the game has come.

    """

    game_over: bool
    who_make_move: PlayerID
    current_winner: Optional[PlayerID]

    def __init__(self) -> None:
        self.game_over = False
        self.who_make_move = FIRST_MOVE
        self.current_winner = None
