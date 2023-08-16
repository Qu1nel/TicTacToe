import sys

import pygame as pg

from src import config
from src.board import GameBoard
from src.config import FIRST_MOVE
from src.game_state import GameState
from src.interface import Interface, InterfaceRaw
from src.misc import Figure, PlayerID, Singleton
from src.player import ComputerPlayer, HumanPlayer
from src.window import Window


class App(InterfaceRaw, metaclass=Singleton):
    """The main class game Tic Tac Toe."""

    def __init__(self) -> None:
        """Init TicTacToe instance."""
        super().__init__()

        self.Window = Window(width=config.WINDOW_WIDTH, height=config.WINDOW_HEIGHT, fps=config.FRAME_PER_SECOND)
        self.GameStates = GameState()
        self.Board = GameBoard()
        self.Interface = Interface()

        self.next_move = FIRST_MOVE
        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()
        self.board = GameBoard()

    def draw_figures(self) -> None:
        """Draws shapes (cross, circle) relative to the state of the board."""
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board[row][col] == Figure.CIRCLE:
                    self._draw_circle(row, col)
                elif self.board[row][col] == Figure.CROSS:
                    self._draw_cross(row, col)

    def _check_vertival_win(self, player: int, draw: bool) -> bool:
        for col in range(self.board.cols):  # vertical win check
            if (self.board[0][col], self.board[1][col], self.board[2][col]) == (player, player, player):
                if draw:
                    self._draw_vertical_winning_line(col, player)
                return True
        return False

    def _check_horizontal_win(self, player: int, draw: bool) -> bool:
        for row in range(self.board.rows):  # horizontal win check
            if (self.board[row][0], self.board[row][1], self.board[row][2]) == (player, player, player):
                if draw:
                    self._draw_horizontal_winning_line(row, player)
                return True
        return False

    def _check_asc_diagonal_win(self, player: int, draw: bool) -> bool:
        # asc diagonal win check
        if (self.board[2][0], self.board[1][1], self.board[0][2]) == (player, player, player):
            if draw:
                self._draw_left_diagonal_line(player)
            return True
        return False

    def _check_desc_diagonal_win(self, player: int, draw: bool) -> bool:
        # desc diagonal win chek
        if (self.board[0][0], self.board[1][1], self.board[2][2]) == (player, player, player):
            if draw:
                self._draw_right_diagonal_line(player)
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
            self._check_vertival_win,
            self._check_horizontal_win,
            self._check_asc_diagonal_win,
            self._check_desc_diagonal_win,
        )
        return any(func(player, draw) for func in check_func)

    def restart(self) -> None:
        """Launch a new game."""
        self.draw_back_ground()
        self.board = GameBoard()
        self.game_over = False
        self.current_winner = -1
        self.next_move = FIRST_MOVE

    def update(self, row: int, col: int, number_player: int) -> None:
        """Update the table, renders it and checks if there is a victory."""
        if self.board.available_square(row, col):
            self.board.mark_square(row, col, number_player)
            if self.check_win(number_player, draw=True):
                self.current_winner = number_player
                self.game_over = True
            self.draw_figures()

    def handle_events(self) -> None:
        """Handle actions entered by the player."""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN and not self.game_over:
                clock_row, clock_col = int(event.pos[1] // self.sq_size), int(event.pos[0] // self.sq_size)
                if self.board.available_square(clock_row, clock_col):
                    self.human_player.make_move(self, clock_row, clock_col)

            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                self.restart()

    def make_moves(self) -> None:
        """Chooses who makes the move."""
        who_made_move = self.next_move
        match who_made_move:
            case PlayerID.COMPUTER if not self.game_over:
                self.computer_player.make_move(self)
            case PlayerID.HUMAN:
                self.handle_events()

    def run(self) -> None:
        """Launch the game."""
        self.draw_back_ground()

        while True:
            self.make_moves()
            pg.display.update()
            self.clock.tick(self.framerate)
