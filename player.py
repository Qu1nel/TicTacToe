import math
import random
from abc import abstractmethod


class Player(object):

    def __init__(self, badge: str):
        """Each player has a badge who he is (cross / circle)"""
        self.badge = badge

    @abstractmethod
    def get_move(self) -> None:
        pass
