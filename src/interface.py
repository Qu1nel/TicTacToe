from functools import partial
from typing import NamedTuple

import pygame as pg

import src.config as c
from src.board import GameBoard
from src.colors import RGBA, Color, get_rgb_color
from src.misc import Figure, SingletonABC
from src.window import Window


class InterfaceColors(NamedTuple):
    """NamedTuple for Colors interface."""

    BackGround: Color | RGBA
    BackGroundLine: Color | RGBA
    Figure: Color | RGBA


class Interface(metaclass=SingletonABC):
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
            Figure=Color.Figure,
        )

        self.bg_line_width = c.LINE_WIDTH
        self.winner_line_width = c.WINNER_LINE_WIDTH
        self.cell_size = c.CELL_SIZE

        self.circle_radius = c.CIRCLE_RADIUS
        self.circle_width = c.CIRCLE_WIDTH

        self.cross_width = c.CROSS_WIDTH

        self.space_cross = c.SPACE_FOR_CROSS

    @staticmethod
    def update_display() -> None:
        """Method alias for pygame.display.update()."""
        pg.display.update()

    def draw_bg(self, window: Window) -> None:
        """Draw BG on window.

        Args:
            window: A window instance.


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

    def draw_figures(self, window: Window, board: GameBoard) -> None:
        """Draws shapes (cross, circle) relative to the state of the board.

        Args:
            window: A windows instance.
            board: A game board.

        """
        for row in range(board.rows):
            for col in range(board.cols):
                if board[row][col] == Figure.CIRCLE:
                    self._draw_circle(window, row, col)
                elif board[row][col] == Figure.CROSS:
                    self._draw_cross(window, row, col)

    def _draw_circle(self, window: Window, row: int, col: int) -> None:
        rgb = get_rgb_color(self.colors.Figure)
        pg.draw.circle(
            surface=window.screen,
            color=rgb,
            center=(col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2),
            radius=self.circle_radius,
            width=self.circle_width,
        )

    def _draw_cross(self, window: Window, row: int, col: int) -> None:
        rgb = get_rgb_color(self.colors.Figure)
        draw_diagonal = partial(
            pg.draw.line,
            surface=window.screen,
            color=rgb,
            width=self.cross_width,
        )

        draw_diagonal(
            start_pos=(
                col * self.cell_size + self.space_cross,
                row * self.cell_size + self.cell_size - self.space_cross,
            ),
            end_pos=(col * self.cell_size + self.cell_size - self.space_cross, row * self.cell_size + self.space_cross),
        )

        draw_diagonal(
            start_pos=(col * self.cell_size + self.space_cross, row * self.cell_size + self.space_cross),
            end_pos=(
                col * self.cell_size + self.cell_size - self.space_cross,
                row * self.cell_size + self.cell_size - self.space_cross,
            ),
        )

    def draw_vertical_winning_line(self, window: Window, col: int) -> None:
        """Draw a vertical victory line on the column `col`.

        Args:
            window: The window where the line will be drawn.
            col: The index of the column where the line will be drawn.

        """
        rgb = get_rgb_color(self.colors.Figure)
        pos_x = col * self.cell_size + self.cell_size // 2
        pg.draw.line(window.screen, rgb, (pos_x, 12), (pos_x, window.height - 12), self.winner_line_width)

    def draw_horizontal_winning_line(self, window: Window, row: int) -> None:
        """Draw a horizontal victory line on the column `row`.

        Args:
            window: The window where the line will be drawn.
            row: The index of the row where the line will be drawn.

        """
        rgb = get_rgb_color(self.colors.Figure)
        pos_y = row * self.cell_size + self.cell_size // 2
        pg.draw.line(window.screen, rgb, (12, pos_y), (window.height - 12, pos_y), self.winner_line_width)

    def draw_left_diagonal_line(self, window: Window) -> None:
        """Draw a left diagonal victory line on the screen.

        Args:
            window: The window where the line will be drawn.

        """
        rgb = get_rgb_color(self.colors.Figure)
        pg.draw.line(window.screen, rgb, (12, window.height - 12), (window.width - 12, 12), self.winner_line_width)

    def draw_right_diagonal_line(self, window: Window) -> None:
        """Draw a right diagonal victory line on the screen.

        Args:
            window: The window where the line will be drawn.

        """
        rgb = get_rgb_color(self.colors.Figure)
        pg.draw.line(window.screen, rgb, (12, 12), (window.width - 12, window.height - 12), self.winner_line_width)
