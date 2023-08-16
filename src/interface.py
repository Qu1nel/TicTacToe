import sys
from abc import abstractmethod
from functools import partial
from typing import NamedTuple

import pygame as pg

import src.config as c
from src import colors
from src.colors import RGBA, Color, get_rgb_color
from src.config import SPACE
from src.game import Game
from src.misc import Singleton
from src.window import Window


class InterfaceRaw(Game):
    """Interface class."""

    sq_size: int
    ln_width: int
    win_ln_width: int
    crcl_color: tuple[int, int, int]
    crss_color: tuple[int, int, int]
    crss_width: int
    crcl_width: int
    crcl_rad: int

    def __init__(self) -> None:
        """Init Interface instance and game class."""
        try:
            assert isinstance(c.SC_WIDTH, int)
            assert isinstance(c.SC_HEIGHT, int)
        except AssertionError:
            sys.exit(1)

        super().__init__(c.SC_WIDTH, c.SC_HEIGHT, c.FRAME_RATE)
        self.sq_size = c.SQUARE_SIZE
        self.win_ln_width = c.WIN_LINE_WIDTH
        self.crcl_color = colors.CIRCLE_COLOR
        self.crss_color = colors.CROSS_COLOR
        self.crss_width = c.CROSS_WIDTH
        self.crcl_width = c.CIRCLE_WIDTH
        self.crcl_rad = c.CIRCLE_RADIUS

    def _draw_circle(self, row: int, col: int) -> None:
        """Draws a circle no the game board."""
        pg.draw.circle(
            surface=self.screen,
            color=self.crcl_color,
            center=(col * self.sq_size + self.sq_size // 2, row * self.sq_size + self.sq_size // 2),
            radius=self.crcl_rad,
            width=self.crcl_width,
        )

    def _draw_cross(self, row: int, col: int) -> None:
        """Draws a cross no the game board."""
        pg.draw.line(
            surface=self.screen,
            color=self.crss_color,
            start_pos=(col * self.sq_size + SPACE, row * self.sq_size + self.sq_size - SPACE),
            end_pos=(col * self.sq_size + self.sq_size - SPACE, row * self.sq_size + SPACE),
            width=self.crss_width,
        )

        pg.draw.line(
            surface=self.screen,
            color=self.crss_color,
            start_pos=(col * self.sq_size + SPACE, row * self.sq_size + SPACE),
            end_pos=(col * self.sq_size + self.sq_size - SPACE, row * self.sq_size + self.sq_size - SPACE),
            width=self.crss_width,
        )

    # 12px is the indentation
    def _draw_vertical_winning_line(self, col: int, player: int) -> None:
        """Draws a vertical line after winning."""
        pos_x = col * self.sq_size + self.sq_size // 2
        color = self.crcl_color if player == 1 else self.crss_color
        pg.draw.line(self.screen, color, (pos_x, 12), (pos_x, self.height - 12), self.win_ln_width)

    # 12px is the indentation
    def _draw_horizontal_winning_line(self, row: int, player: int) -> None:
        """Draws a horizontal line after winning."""
        pos_y = row * self.sq_size + self.sq_size // 2
        color = self.crcl_color if player == 1 else self.crss_color
        pg.draw.line(self.screen, color, (12, pos_y), (self.height - 12, pos_y), self.win_ln_width)

    # 12px is the indentation
    def _draw_left_diagonal_line(self, player: int) -> None:
        """Draws a left diagonal (Top left) line after winning."""
        color = self.crcl_color if player == 1 else self.crss_color
        pg.draw.line(self.screen, color, (12, self.height - 12), (self.width - 12, 12), self.win_ln_width)

    # 12px is the indentation
    def _draw_right_diagonal_line(self, player: int) -> None:
        """Draws a right diagonal (Top right) line after winning."""
        color = self.crcl_color if player == 1 else self.crss_color
        pg.draw.line(self.screen, color, (12, 12), (self.width - 12, self.height - 12), self.win_ln_width)

    @abstractmethod
    def draw_figures(self) -> None:
        """Draws the main figures (circle and cross)."""


class InterfaceColors(NamedTuple):
    """NamedTuple for Colors interface."""

    BackGround: Color | RGBA
    BackGroundLine: Color | RGBA


class Interface(metaclass=Singleton):
    """Flex interface class.

    Attributes:
        colors: Set a using colors.
        bg_line_width: A width line on window.
        cell_size: A width and height of cell on window.

    """

    colors: InterfaceColors
    bg_line_width: int
    cell_size: int

    def __init__(self) -> None:
        self.colors = InterfaceColors(
            BackGround=Color.BG,
            BackGroundLine=Color.BG_LINE,
        )

        self.bg_line_width = c.LINE_WIDTH
        self.cell_size = c.CELL_SIZE

    @staticmethod
    def update_display() -> None:
        """Method alias for pygame.display.update()."""
        pg.display.update()

    def draw_bg(self, window: Window) -> None:
        """Draw BG on window.

        Args:
            window: A window instance


        Raises:
            TypeError: If self.colors.BackGround is not Color or RGBA class.

        """
        rgb = get_rgb_color(self.colors.BackGround)
        window.screen.fill(rgb)
        self._draw_bg_lines(window)
        self.update_display()

    def _draw_bg_lines(self, window: Window) -> None:
        rgb = get_rgb_color(self.colors.BackGroundLine)

        draw_bg_line = partial(
            pg.draw.line,
            surface=window.screen,
            color=rgb,
            width=self.bg_line_width,
        )

        horizontals_coords = (
            {
                "start": (0, self.cell_size),
                "end": (window.width, self.cell_size),
            },
            {
                "start": (0, 2 * self.cell_size),
                "end": (window.width, 2 * self.cell_size),
            },
        )

        vertical_coords = (
            {
                "start": (self.cell_size, 0),
                "end": (self.cell_size, window.height),
            },
            {
                "start": (2 * self.cell_size, 0),
                "end": (2 * self.cell_size, window.height),
            },
        )

        for coords in horizontals_coords + vertical_coords:
            draw_bg_line(
                start_pos=coords["start"],
                end_pos=coords["end"],
            )
