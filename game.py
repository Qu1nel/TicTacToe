from abc import abstractmethod
import pygame


class Game(object):
    """A class with all the main attributes of the game (game window)"""
    caption: str
    width: int
    height: int
    framerate: int

    def __init__(self, caption, width, height, framerate=60):
        pygame.init()
        pygame.display.set_caption(caption)
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.framerate = framerate
        self.width = width
        self.height = height
        self.player = 1
        self.game_over = False
        self.current_winner = None

    @abstractmethod
    def minimax(self, player: int) -> dict:
        """Algorithm for tic-tac-toe, based on minimax"""
        pass

    @abstractmethod
    def update(self, row: int, col: int) -> None:
        """Updates the table, renders it and checks if there is a victory"""
        pass

    @abstractmethod
    def computer(self) -> None:
        """Makes a move for the opponent (computer)"""
        pass

    @abstractmethod
    def handle_events(self) -> None:
        """Handles actions entered by the player"""
        pass

    @abstractmethod
    def restart(self) -> None:
        """Launches a new game"""
        pass

    def run(self) -> None:
        """Launches the game"""
        pass
