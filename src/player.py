import math
import random
import sys
import time
from dataclasses import dataclass
from typing import Final

import numpy as np
import pygame as pg

from src import config
from src.app import AppBase
from src.board import GameBoard
from src.game_state import GameState
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

    def make_move(self, states: GameState, game: AppBase, row: int, col: int) -> None:
        """Make move for Human."""
        game.update(row, col, self.number)
        states.who_make_move = PlayerID.COMPUTER

    def step(self, states: GameState, board: GameBoard, game: AppBase) -> None:
        """Handles events from the user, starts the move from the person.

        Args:
            states: Some game states.
            board: Game board.
            game: Game itself.

        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN and not states.game_over:
                clock_row = event.pos[1] // game.Interface.cell_size
                clock_col = event.pos[0] // game.Interface.cell_size

                if board.available_square(clock_row, clock_col):
                    self.make_move(states=states, game=game, row=clock_row, col=clock_col)

            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                game.restart()


class ComputerPlayer(Player):
    """Computer pseudo-AI player."""

    def __init__(self) -> None:
        human_figure = config.PLAYER_FIGURE
        computer_figure = Figure.CIRCLE if human_figure.value == Figure.CROSS.value else Figure.CROSS
        super().__init__(figure=computer_figure, number=PlayerID.COMPUTER)

    def minimax(self, states: GameState, game: AppBase, board: GameBoard, player: PlayerID) -> dict:
        """Algorithm for tic-tac-toe, based on minimax."""
        best_player = self.number
        other_player = PlayerID.HUMAN if player == PlayerID.COMPUTER else PlayerID.COMPUTER

        if states.current_winner == other_player:  # first we want to check if the previous move is a winner
            count_zeros = np.sum(board.get_board == 0) + 1
            return {"position": None, "score": 1 * count_zeros if other_player == best_player else -1 * count_zeros}

        if 0 not in board.get_board:
            return {"position": None, "score": 0}

        if player == best_player:
            best_move = {"position": None, "score": -math.inf}  # each score should maximize
        else:
            # each score should minimize
            best_move = {"position": None, "score": math.inf}

        straight_board = [digit for row in board.get_board for digit in row]
        for possible_move in [idx for idx, digit in enumerate(straight_board) if digit == 0]:
            board.mark_square(possible_move // 3, possible_move % 3, player)
            if game.check_win(player, draw=False):
                states.current_winner = player

            sim_score = self.minimax(states=states, game=game, board=board, player=other_player)

            # undo move
            board[possible_move // 3][possible_move % 3] = 0
            states.current_winner = None

            # this represents the move optimal next move
            sim_score["position"] = possible_move

            if player == best_player:
                if sim_score["score"] > best_move["score"]:
                    best_move = sim_score
            elif sim_score["score"] < best_move["score"]:
                best_move = sim_score

        return best_move

    def make_move(self, states: GameState, game: AppBase, board: GameBoard) -> None:
        """Make a move for the opponent (computer)."""
        if not states.game_over:
            print("in make_move")
            time.sleep(0.2)

            if np.sum(board.get_board == 0) != MAX_SUM:
                coordinates = self.minimax(states=states, game=game, board=board, player=self.number)["position"]
            else:
                coordinates = random.randint(0, 8)

            if coordinates is not None:
                clock_row, clock_col = coordinates // 3, coordinates % 3
                game.update(clock_row, clock_col, self.number)

            states.who_make_move = PlayerID.HUMAN

    def step(self, states: GameState, board: GameBoard, game: AppBase) -> None:
        """Start the move from the computer.

        Args:
            states: Some game states.
            board: Game board.
            game: Game itself.

        """
        if not states.game_over:
            self.make_move(states=states, game=game, board=board)
