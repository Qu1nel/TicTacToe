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
        raise NotImplemented

    def _draw_vertical_winning_line(self) -> None:
        """Draws a vertical line after winning"""
        raise NotImplemented

    def _draw_horizontal_winning_line(self) -> None:
        """Draws a horizontal line after winning"""
        raise NotImplemented

    def _draw_left_diagonal_line(self) -> None:
        """Draws a left diagonal (Top left) line after winning"""
        raise NotImplemented

    def _draw_right_diagonal_line(self) -> None:
        """Draws a right diagonal (Top right) line after winning"""
        raise NotImplemented

    def draw_figures(self) -> None:
        """Draws the main figures (circle and cross)"""
        raise NotImplemented
