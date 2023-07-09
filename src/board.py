import numpy as np
import numpy.typing as npt

import src.config as con


class GameBoard:
    """Representation of the playing field."""

    __board: npt.NDArray[np.float64]
    cols: int
    rows: int

    def __init__(self) -> None:
        """Init GameBoard instance."""
        self.__board = np.zeros((con.BOARD_ROWS, con.BOARD_COLS))
        self.rows = con.BOARD_ROWS
        self.cols = con.BOARD_COLS

    def __getitem__(self, item: int) -> npt.NDArray[np.float64]:
        """Return self[item].

        Args:
            item: Index to get row board.

        """
        result: npt.NDArray[np.float64] = self.__board[item]
        return result

    def __setitem__(self, key: int, value: int) -> None:
        """Provide self[key] = value.

        Args:
            key: Number of column
            value: Value between 0 and 1

        """
        self.get_board[key] = value

    @property
    def get_board(self) -> npt.NDArray[np.float64]:
        """Return main game board."""
        return self.__board

    def mark_square(self, row: int, col: int, player: int) -> None:
        """Mark the square of the board by the player."""
        self[row][col] = player

    def available_square(self, row: int, col: int) -> bool:
        """Check a square to see if it not is empty."""
        return not self.__board[row][col]
