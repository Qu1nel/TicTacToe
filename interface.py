from typing import Union

import pygame as pyg

import colors
import config as con
from game import Game


class Interface(Game):
    sq_size: int
    ln_width: int
    win_ln_width: int
    crcl_color: Union[tuple[int], str, list[int]]
    crss_color: Union[tuple[int], str, list[int]]
    crss_width: int
    crcl_width: int
    crcl_rad: int

    def __init__(self):
        super().__init__(con.CAPTION, con.SC_WIDTH, con.SC_HEIGHT, con.FRAME_RATE)
        self.sq_size = con.SQUARE_SIZE
        self.ln_width = con.LINE_WIDTH
        self.win_ln_width = con.WIN_LINE_WIDTH
        self.crcl_color = colors.CIRCLE_COLOR
        self.crss_color = colors.CROSS_COLOR
        self.crss_width = con.CROSS_WIDTH
        self.crcl_width = con.CIRCLE_WIDTH
        self.crcl_rad = con.CIRCLE_RADIUS

    def draw_BG(self) -> None:
        """Draws the background"""
        self.screen.fill(colors.BG_COLOR)
        self._draw_lines()

    def _draw_lines(self) -> None:
        """Draws the lines for BG"""
        # horizontals
        pyg.draw.line(surface=self.screen, color=colors.BG_LINE_COLOR,
                      start_pos=(0, self.sq_size), end_pos=(self.width, self.sq_size),
                      width=self.win_ln_width)
        pyg.draw.line(surface=self.screen, color=colors.BG_LINE_COLOR,
                      start_pos=(0, self.sq_size * 2), end_pos=(self.width, self.sq_size * 2),
                      width=self.win_ln_width)
        # vertical
        pyg.draw.line(surface=self.screen, color=colors.BG_LINE_COLOR,
                      start_pos=(self.sq_size, 0), end_pos=(self.sq_size, self.height),
                      width=self.win_ln_width)
        pyg.draw.line(surface=self.screen, color=colors.BG_LINE_COLOR,
                      start_pos=(self.sq_size * 2, 0), end_pos=(self.sq_size * 2, self.height),
                      width=self.win_ln_width)

    def _draw_vertical_winning_line(self, col: int, player: int) -> None:
        """Draws a vertical line after winning"""
        raise NotImplemented

    def _draw_horizontal_winning_line(self, row: int, player: int) -> None:
        """Draws a horizontal line after winning"""
        raise NotImplemented

    def _draw_left_diagonal_line(self, player: int) -> None:
        """Draws a left diagonal (Top left) line after winning"""
        raise NotImplemented

    def _draw_right_diagonal_line(self, player: int) -> None:
        """Draws a right diagonal (Top right) line after winning"""
        raise NotImplemented

    def _draw_circle(self):
        raise NotImplemented

    def _draw_cross(self):
        raise NotImplemented

    def draw_figures(self) -> None:
        """Draws the main figures (circle and cross)"""
        raise NotImplemented
