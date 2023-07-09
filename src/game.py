from abc import abstractmethod

import pygame

from src.board import GameBoard


class Game:
    """A class with all the main attributes of the game (game window)."""

    caption: str
    width: int
    height: int
    framerate: int
    board: GameBoard
    go_first: str

    def __init__(self, caption: str, width: int, height: int, framerate: int = 60) -> None:
        """Init Game instance."""
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.framerate = framerate
        self.width = width
        self.height = height
        self.game_over = False
        self.current_winner = -1

    @abstractmethod
    def update(self, row: int, col: int, number_player: int) -> None:
        """Update the table, renders it and checks if there is a victory."""

    @abstractmethod
    def handle_events(self) -> None:
        """Handle actions entered by the player."""

    @abstractmethod
    def restart(self) -> None:
        """Launch a new game."""

    @abstractmethod
    def check_win(self, player: int, draw: bool = True) -> bool:
        """Check win."""

    def run(self) -> None:
        """Launch the game."""
