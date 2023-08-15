import math
import random
import time
from dataclasses import dataclass
from typing import Final

import numpy as np

from src import config
from src.game import Game
from src.misc import Figure, PlayerID

MAX_SUM: Final[int] = 9


@dataclass(slots=True, frozen=True)
class Player:
    """Player class."""

    figure: Figure
    number: PlayerID


class HumanPlayer(Player):
    """Human player."""

    def __init__(self) -> None:
        super().__init__(figure=config.PLAYER_FIGURE, number=PlayerID.HUMAN)

    def make_move(self, game: Game, row: int, col: int) -> None:
        """Make move for Human."""
        game.update(row, col, self.number)
        game.next_move = PlayerID.COMPUTER


class ComputerPlayer(Player):
    """Coumputer pseudo-AI player."""

    def __init__(self) -> None:
        computer_figure = Figure.CIRCLE if config.PLAYER_FIGURE == Figure.CROSS else Figure.CROSS
        super().__init__(figure=computer_figure, number=PlayerID.COMPUTER)

    def minimax(self, game: Game, player: int) -> dict:
        """Algorithm for tic-tac-toe, based on minimax."""
        best_player = self.number
        other_player = PlayerID.HUMAN if player == PlayerID.COMPUTER else PlayerID.COMPUTER

        if game.current_winner == other_player:  # first we want to check if the previous move is a winner
            count_zeros = np.sum(game.board.get_board == 0) + 1
            return {"position": None, "score": 1 * count_zeros if other_player == best_player else -1 * count_zeros}

        if 0 not in game.board.get_board:
            return {"position": None, "score": 0}

        if player == best_player:
            best_move = {"position": None, "score": -math.inf}  # each score should maximize
        else:
            # each score should minimize
            best_move = {"position": None, "score": math.inf}

        straight_board = [digit for row in game.board.get_board for digit in row]
        for possible_move in [indx for indx, digit in enumerate(straight_board) if digit == 0]:
            game.board.mark_square(possible_move // 3, possible_move % 3, player)
            if game.check_win(player, draw=False):
                game.current_winner = player

            sim_score = self.minimax(game, other_player)

            # undo move
            game.board[possible_move // 3][possible_move % 3] = 0
            game.current_winner = -1

            # this represents the move optimal next move
            sim_score["position"] = possible_move

            if player == best_player:
                if sim_score["score"] > best_move["score"]:
                    best_move = sim_score
            elif sim_score["score"] < best_move["score"]:
                best_move = sim_score

        return best_move

    def make_move(self, game: Game) -> None:
        """Make a move for the opponent (computer)."""
        if not game.game_over:
            time.sleep(0.2)

            if np.sum(game.board.get_board == 0) != MAX_SUM:
                coordinates = self.minimax(game, self.number)["position"]  # MINIMAX
            else:
                coordinates = random.randint(0, 8)

            if coordinates is not None:
                clock_row, clock_col = coordinates // 3, coordinates % 3
                game.update(clock_row, clock_col, self.number)

            game.next_move = PlayerID.HUMAN
