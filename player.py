import math
import random
import time
from abc import abstractmethod

import numpy as np

from game import Game
from config import FIGURE_PLAYER, FIGURE_COMPUTER


class Player(object):

    def __init__(self, badge: tuple[str, int]):
        """Each player has a badge who he is (cross / circle)"""
        self.badge = badge

    @staticmethod
    @abstractmethod
    def make_move(*args, **kwargs) -> None:
        pass


class HumanPlayer(Player):

    def __init__(self):
        super().__init__(FIGURE_PLAYER)

    @staticmethod
    def make_move(game: Game, row: int, col: int) -> None:
        game.update(row, col)
        game.go_first = 'COMPUTER'


class ComputerPlayer(Player):

    def __init__(self):
        super().__init__(FIGURE_COMPUTER)

    @staticmethod
    def minimax(game: Game, player: int) -> dict:
        """Algorithm for tic-tac-toe, based on minimax"""
        best_player = game.player
        other_player = 1 if player == 2 else 2

        if game.current_winner == other_player:  # first we want to check if the previous move is a winner
            count_zeros = np.sum(game.board.get_board == 0) + 1
            return dict(position=None, score=1 * count_zeros if other_player == best_player else -1 * count_zeros)

        elif 0 not in game.board.get_board:
            return dict(position=None, score=0)

        if player == best_player:
            best_move = dict(position=None, score=-math.inf)  # each score should maximize
        else:
            best_move = dict(position=None, score=math.inf)  # each score should minimize

        straight_board = [digit for row in self.board.get_board for digit in row]
        for possible_move in [indx for indx, digit in enumerate(straight_board) if digit == 0]:

            game.board.mark_square(possible_move // 3, possible_move % 3, player)
            if game.check_win(player, draw=False):
                game.current_winner = player

            sim_score = self.minimax(other_player)

            # undo move
            self.board[possible_move // 3][possible_move % 3] = 0
            self.current_winner = None

            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == best_player:
                if sim_score['score'] > best_move['score']:
                    best_move = sim_score
            else:
                if sim_score['score'] < best_move['score']:
                    best_move = sim_score

        return best_move

    def make_move(self, game: Game) -> None:
        """Makes a move for the opponent (computer)"""
        if not game.game_over:
            time.sleep(.2)

            if np.sum(game.board.get_board == 0) != 9:
                coordinates = game.minimax(game, game.player)['position']  # MINIMAX
            else:
                coordinates = random.randint(0, 8)

            if coordinates is not None:
                clock_row, clock_col = coordinates // 3, coordinates % 3
                game.update(clock_row, clock_col)

            game.go_first = 'PLAYER'
