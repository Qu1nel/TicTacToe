import numpy as np
from numpy import ndarray

import src.config as con


class GameBoard(object):
    __board: ndarray
    cols: int
    rows: int

    def __init__(self):
        self.__board = np.zeros((con.BOARD_ROWS, con.BOARD_COLS))
        self.rows = con.BOARD_ROWS
        self.cols = con.BOARD_COLS

    def __getitem__(self, item):
        return self.get_board[item]

    def __setitem__(self, key, value):
        self.get_board[key] = value

    @property
    def get_board(self) -> ndarray:
        return self.__board

    def mark_square(self, row: int, col: int, player: int) -> None:
        """Marks the square of the board by the player"""
        self[row][col] = player

    def available_square(self, row: int, col: int) -> bool:
        """Checks a square to see if it not is empty"""
        return self[row][col] == 0
