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
