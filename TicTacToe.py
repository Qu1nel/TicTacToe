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

    def update(self, row: int, col: int):
        """Updates the table, renders it and checks if there is a victory"""
        if self.board.available_square(row, col):
            self.board.mark_square(row, col, self.player)
            ...

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
