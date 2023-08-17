from typing import Never, assert_never

from src import config
from src.app import AppBase
from src.board import GameBoard
from src.config import FIRST_MOVE
from src.game_state import GameState
from src.interface import Interface
from src.misc import PlayerID
from src.player import ComputerPlayer, HumanPlayer
from src.window import Window


class App(AppBase):
    """The main class game Tic Tac Toe."""

    def __init__(self) -> None:
        """Init TicTacToe instance."""
        super().__init__()

        self.Window = Window(width=config.WINDOW_SIZE, height=config.WINDOW_SIZE, fps=config.FRAME_PER_SECOND)
        self.GameStates = GameState()
        self.Board = GameBoard()
        self.Interface = Interface()

        self.HumanPlayer = HumanPlayer()
        self.ComputerPlayer = ComputerPlayer()

    def _check_vertical_win(self, player: int, draw: bool) -> bool:
        for col in range(self.Board.cols):  # vertical win check
            if (self.Board[0][col], self.Board[1][col], self.Board[2][col]) == (player, player, player):
                if draw:
                    self.Interface.draw_vertical_winning_line(window=self.Window, col=col)
                return True
        return False

    def _check_horizontal_win(self, player: int, draw: bool) -> bool:
        for row in range(self.Board.rows):  # horizontal win check
            if (self.Board[row][0], self.Board[row][1], self.Board[row][2]) == (player, player, player):
                if draw:
                    self.Interface.draw_horizontal_winning_line(window=self.Window, row=row)
                return True
        return False

    def _check_asc_diagonal_win(self, player: int, draw: bool) -> bool:
        if (self.Board[2][0], self.Board[1][1], self.Board[0][2]) == (player, player, player):
            if draw:
                self.Interface.draw_left_diagonal_line(window=self.Window)
            return True
        return False

    def _check_desc_diagonal_win(self, player: int, draw: bool) -> bool:
        if (self.Board[0][0], self.Board[1][1], self.Board[2][2]) == (player, player, player):
            if draw:
                self.Interface.draw_right_diagonal_line(window=self.Window)
            return True
        return False

    def check_win(self, player: int, draw: bool = True) -> bool:
        """Draws a line in case of victory.

        Args:
        ----
        player (int): The player who made the move
        draw (bool): A flag that determines whether to draw when a
            victory is detected (bool)

        Returns:
        -------
            The True if Victory else False
        """
        check_func = (
            self._check_vertical_win,
            self._check_horizontal_win,
            self._check_asc_diagonal_win,
            self._check_desc_diagonal_win,
        )
        return any(func(player, draw) for func in check_func)

    def restart(self) -> None:
        """Launch a new game."""
        self.Interface.draw_bg(window=self.Window)
        self.Board = GameBoard()

        self.GameStates.game_over = False
        self.GameStates.who_make_move = FIRST_MOVE
        self.GameStates.current_winner = None

    def update(self, row: int, col: int, number_player: PlayerID) -> None:
        """Update the table, renders it and checks if there is a victory."""
        if self.Board.available_square(row, col):
            self.Board.mark_square(row, col, number_player)
            if self.check_win(number_player, draw=True):
                self.GameStates.game_over = True
                self.GameStates.current_winner = number_player
            self.Interface.draw_figures(window=self.Window, board=self.Board)

    def make_moves(self) -> None:
        """Chooses who makes the move."""
        match self.GameStates.who_make_move:
            case PlayerID.COMPUTER:
                self.ComputerPlayer.step(states=self.GameStates, board=self.Board, game=self)
            case PlayerID.HUMAN:
                self.HumanPlayer.step(states=self.GameStates, board=self.Board, game=self)
            case _ as never:
                assert_never(never)

    def run(self) -> Never:
        """Launch the game."""
        self.Interface.draw_bg(window=self.Window)

        while True:
            self.make_moves()
            self.Interface.update_display()
            self.Window.set_fps()
