from abc import abstractmethod

import pygame


class Game:
    """A class with all the main attributes of the game (game window)."""

    caption: str
    width: int
    height: int
    framerate: int

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
        self.current_winner = None

    @abstractmethod
    def update(self, row: int, col: int, number_player: int) -> None:
        """Update the table, renders it and checks if there is a victory."""

    @abstractmethod
    def handle_events(self) -> None:
        """Handle actions entered by the player."""

    @abstractmethod
    def restart(self) -> None:
        """Launch a new game."""

    def run(self) -> None:
        """Launch the game."""
