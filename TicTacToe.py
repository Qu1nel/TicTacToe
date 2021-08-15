import sys
import math
import time
import random
import pygame
import numpy as np
import config as c
from interface import Interface
from board import GameBoard


class TicTacToe(Interface):

    def __init__(self):
        super().__init__()
        self.board = GameBoard()

    def restart(self):
        """Launches a new game"""
        self.draw_BG()
        self.board = GameBoard()
        self.player = 1
        self.game_over = False

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
                    self._draw_horizontal_winning_line(col, player)
                return True

        # asc diagonal win check
        if (self.board[2][0], self.board[1][1], self.board[0][2]) == (player, player, player):
            if draw:
                self._draw_asc_diagonal(self.player)
            return True

        # desc diagonal win chek
        if (self.board[0][0], self.board[1][1], self.board[2][2]) == (player, player, player):
            if draw:
                self._draw_desc_diagonal(self.player)
            return True

        return False

    def update(self, row: int, col: int):
        """Updates the table, renders it and checks if there is a victory"""
        if self.board.available_square(row, col):
            self.board.mark_square(row, col, self.player)
            if self.check_win(self.player, draw=True):
                pass

    def handle_events(self) -> None:
        """Handles actions entered by the player"""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                clock_row, clock_col = int(event.pos[1] // self.sq_size), int(event.pos[0] // self.sq_size)
                self.update(clock_row, clock_col)

            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_r:
                    self.restart()

    def computer(self):
        """Makes a move for the opponent (computer)"""
        pass

    def run(self) -> None:
        """Launches the game"""
        self.draw_BG()
        while True:
            pygame.display.update()

            self.computer()
            self.handle_events()

            self.clock.tick(self.framerate)


def main():
    TicTacToe().run()


if __name__ == '__main__':
    main()
