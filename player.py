import math
import random
from abc import abstractmethod

from config import FIGURE_PLAYER, FIGURE_COMPUTER


class Player(object):

    def __init__(self, badge):
        """Each player has a badge who he is (cross / circle)"""
        self.badge = badge


class HumanPlayer(Player):

    def __init__(self):
        super().__init__(FIGURE_PLAYER)


class ComputerPlayer(Player):

    def __init__(self):
        super().__init__(FIGURE_COMPUTER)
