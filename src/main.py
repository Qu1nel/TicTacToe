import sys
from typing import Final

import pygame

from src.board import GameBoard
from src.config import GO_FIRST
from src.interface import Interface
from src.player import ComputerPlayer, HumanPlayer

CROSS: Final[int] = 2
CIRCLE: Final[int] = 1


class TicTacToe(Interface):
    """The main class game Tic Tac Toe."""

    def __init__(self) -> None:
        """Init TicTacToe instance."""
        super().__init__()
        self.go_first = GO_FIRST
        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()
        self.board = GameBoard()

    def draw_figures(self) -> None:
        """Draws shapes (cross, circle) relative to the state of the board."""
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board[row][col] == CIRCLE:
                    self._draw_circle(row, col)
                elif self.board[row][col] == CROSS:
                    self._draw_cross(row, col)

    def check_win(self, player: int, draw: bool = True) -> bool:
        """Draws a line in case of victory.

        Args:
        ----
        player (int): The player who made the move
        draw (bool): A flag that determines whether to draw when a
            victory is detected (bool)

        Returns:
        -------
            The True if else False

        """
        for col in range(self.board.cols):  # vertical win check
            if (self.board[0][col], self.board[1][col], self.board[2][col]) == (player, player, player) and draw:
                self._draw_vertical_winning_line(col, player)
                return True

        for row in range(self.board.rows):  # horizontal win check
            if (self.board[row][0], self.board[row][1], self.board[row][2]) == (player, player, player) and draw:
                self._draw_horizontal_winning_line(row, player)
                return True

        # asc diagonal win check
        if (self.board[2][0], self.board[1][1], self.board[0][2]) == (player, player, player) and draw:
            self._draw_left_diagonal_line(player)
            return True

        # desc diagonal win chek
        if (self.board[0][0], self.board[1][1], self.board[2][2]) == (player, player, player) and draw:
            self._draw_right_diagonal_line(player)
            return True

        return False

    def restart(self) -> None:
        """Launch a new game."""
        self.draw_BG()
        self.board = GameBoard()
        self.game_over = False
        self.current_winner = None
        self.go_first = GO_FIRST

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                clock_row, clock_col = int(
                    event.pos[1] // self.sq_size), int(event.pos[0] // self.sq_size)
                if self.board.available_square(clock_row, clock_col):
                    self.human_player.make_move(self, clock_row, clock_col)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                self.restart()

    def make_moves(self) -> None:
        """Chooses who makes the move."""
        if self.go_first == "COMPUTER" and not self.game_over:
            self.computer_player.make_move(self)
        elif self.go_first == "PLAYER":
            self.handle_events()

    def run(self) -> None:
        """Launch the game."""
        self.draw_BG()
        while True:
            self.make_moves()

            pygame.display.update()
            self.clock.tick(self.framerate)


def main() -> None:
    """Enter point in game."""
    TicTacToe().run()
