"""Package providing all the necessary packages for a game of tic-tac-toe."""
import sys
from pathlib import Path

import pygame as pg

from src.main import App

__author__ = "Qu1nel"
__version__ = "2.1"


def resource_path(relative_path: Path) -> Path:
    """Function for working paths inside an exe for python."""
    base_path = Path(getattr(sys, "_MEIPASS", ".")).absolute()
    return base_path.joinpath(relative_path)


pg.init()

icon_name = "icon.png"
icon_folder_name = "icons"
icon_path = Path(icon_folder_name) / Path(icon_name)

try:
    icon = pg.image.load(resource_path(icon_path))
    pg.display.set_icon(icon)
except FileNotFoundError:
    pass

pg.display.set_caption("TicTacToe")

game = App()
