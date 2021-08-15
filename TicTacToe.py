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

    def minimax(self, player: int) -> dict:
        """Algorithm for tic-tac-toe, based on minimax"""
        best_player = self.player
        other_player = 1 if player == 2 else 2

        if self.current_winner == other_player:  # first we want to check if the previous move is a winner
            count_zeros = np.sum(self.board.get_board == 0) + 1
            return dict(position=None, score=1 * count_zeros if other_player == best_player else -1 * count_zeros)

        elif 0 not in self.board.get_board:
            return dict(position=None, score=0)

        if player == best_player:
            best_move = dict(position=None, score=-math.inf)  # each score should maximize
        else:
            best_move = dict(position=None, score=math.inf)  # each score should minimize

    def computer(self) -> None:
        """Makes a move for the opponent (computer)"""
        if self.player == 1 and not self.game_over:
            time.sleep(.5)
            print(np.sum(self.board.get_board == 0))

            if np.sum(self.board.get_board == 0) == 9:
                coordinates = random.randint(0, 8)  # MINIMAX
            else:
                coordinates = random.randint(0, 8)

            assert isinstance(coordinates, (int, float))

            clock_row, clock_col = coordinates // 3, coordinates % 3
            self.update(clock_row, clock_col)

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
                self._draw_left_diagonal_line(self.player)
            return True

        # desc diagonal win chek
        if (self.board[0][0], self.board[1][1], self.board[2][2]) == (player, player, player):
            if draw:
                self._draw_right_diagonal_line(self.player)
            return True

        return False

    def update(self, row: int, col: int) -> None:
        """Updates the table, renders it and checks if there is a victory"""
        if self.board.available_square(row, col):
            self.board.mark_square(row, col, self.player)
            if self.check_win(self.player, draw=True):
                self.current_winner = self.player
                self.game_over = True
            self.player = self.player % 2 + 1
            self.draw_figures()

    def restart(self) -> None:
        """Launches a new game"""
        self.draw_BG()
        self.board = GameBoard()
        self.player = 1
        self.game_over = False
        self.current_winner = None

    def handle_events(self) -> None:
        """Handles actions entered by the player"""
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over and self.player == 2:
                clock_row, clock_col = int(event.pos[1] // self.sq_size), int(event.pos[0] // self.sq_size)
                self.update(clock_row, clock_col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.restart()

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
