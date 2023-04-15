import sys
import math
import time
import random
import pygame
import numpy as np
from config import GO_FIRST
from interface import Interface
from board import GameBoard
from player import HumanPlayer, ComputerPlayer


class TicTacToe(Interface):

    def __init__(self):
        super().__init__()
        self.go_first = GO_FIRST
        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()
        self.board = GameBoard()

    def draw_figures(self) -> None:
        """Draws shapes (cross, circle) relative to the state of the board"""
        for row in range(self.board.rows):
            for col in range(self.board.cols):
                if self.board[row][col] == 1:
                    self._draw_circle(row, col)
                elif self.board[row][col] == 2:
                    self._draw_cross(row, col)

    def check_win(self, player: int, draw=True) -> bool:
        """The function determines whether there has been a victory
        and draws a victory line for the winning piece using the flag.

        :param player: The player who made the move (int)
        :param draw: A flag that determines whether to draw when a victory is detected (bool)
        :return: bool
        """
        for col in range(self.board.cols):  # vertical win check
            if (self.board[0][col], self.board[1][col], self.board[2][col]) == (player, player, player):
                if draw:
                    self._draw_vertical_winning_line(col, player)
                return True

        for row in range(self.board.rows):  # horizontal win check
            if (self.board[row][0], self.board[row][1], self.board[row][2]) == (player, player, player):
                if draw:
                    self._draw_horizontal_winning_line(row, player)
                return True

        # asc diagonal win check
        if (self.board[2][0], self.board[1][1], self.board[0][2]) == (player, player, player):
            if draw:
                self._draw_left_diagonal_line(player)
            return True

        # desc diagonal win chek
        if (self.board[0][0], self.board[1][1], self.board[2][2]) == (player, player, player):
            if draw:
                self._draw_right_diagonal_line(player)
            return True

        return False

    def restart(self) -> None:
        """Launches a new game"""
        self.draw_BG()
        self.board = GameBoard()
        self.game_over = False
        self.current_winner = None
        self.go_first = GO_FIRST

    def update(self, row: int, col: int, number_player: int) -> None:
        """Updates the table, renders it and checks if there is a victory"""
        if self.board.available_square(row, col):
            self.board.mark_square(row, col, number_player)
            if self.check_win(number_player, draw=True):
                self.current_winner = number_player
                self.game_over = True
            self.draw_figures()

    def handle_events(self) -> None:
        """Handles actions entered by the player"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                clock_row, clock_col = int(event.pos[1] // self.sq_size), int(event.pos[0] // self.sq_size)
                if self.board.available_square(clock_row, clock_col):
                    self.human_player.make_move(self, clock_row, clock_col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart()

    def make_moves(self) -> None:
        if self.go_first == 'COMPUTER' and not self.game_over:
            self.computer_player.make_move(self)
        elif self.go_first == 'PLAYER':
            self.handle_events()

    def run(self) -> None:
        """Launches the game"""
        self.draw_BG()
        while True:
            self.make_moves()

            pygame.display.update()
            self.clock.tick(self.framerate)


def main():
    TicTacToe().run()


if __name__ == '__main__':
    main()
