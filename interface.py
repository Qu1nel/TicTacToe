from typing import Union

import pygame as pyg

import colors
import config as c
from config import SPACE
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
        super().__init__(c.CAPTION, c.SC_WIDTH, c.SC_HEIGHT, c.FRAME_RATE)
        self.sq_size = c.SQUARE_SIZE
        self.ln_width = c.LINE_WIDTH
        self.win_ln_width = c.WIN_LINE_WIDTH
        self.crcl_color = colors.CIRCLE_COLOR
        self.crss_color = colors.CROSS_COLOR
        self.crss_width = c.CROSS_WIDTH
        self.crcl_width = c.CIRCLE_WIDTH
        self.crcl_rad = c.CIRCLE_RADIUS

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

    def _draw_circle(self, row: int, col: int) -> None:
        """draws a circle no the game board"""
        pyg.draw.circle(surface=self.screen, color=self.crcl_color,
                        center=(col * self.sq_size + self.sq_size // 2, row * self.sq_size + self.sq_size // 2),
                        radius=self.crcl_rad, width=self.crcl_width)

    def _draw_cross(self, row: int, col: int) -> None:
        """draws a cross no the game board"""
        pyg.draw.line(surface=self.screen, color=self.crss_color,
                      start_pos=(col * self.sq_size + SPACE, row * self.sq_size + self.sq_size - SPACE),
                      end_pos=(col * self.sq_size + self.sq_size - SPACE, row * self.sq_size + SPACE),
                      width=self.crss_width)

        pyg.draw.line(surface=self.screen, color=self.crss_color,
                      start_pos=(col * self.sq_size + SPACE, row * self.sq_size + SPACE),
                      end_pos=(col * self.sq_size + self.sq_size - SPACE, row * self.sq_size + self.sq_size - SPACE),
                      width=self.crss_width)

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

    def draw_figures(self) -> None:
        """Draws the main figures (circle and cross)"""
        raise NotImplemented
