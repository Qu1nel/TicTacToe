import json
from pathlib import Path
from typing import Any, Final

from src.misc import Figure, PlayerID

APP_PATH = Path(__file__).resolve().parent

DEFAULT_SETT = {
    "first_move": "COMPUTER",
    "figure_player": "cross",
    "width_window": 600,
}

SC_WIDTH: int = 0
SC_HEIGHT: int = 0
LENTH_BOARD: Final[int] = 3

FIRST_MOVE = PlayerID.COMPUTER  # COMPUTER or PLAYER
PLAYER_FIGURE = Figure.CIRCLE  # CIRCLE or CROSS

WINDOW_WIDTH: Final[int] = 720
WINDOW_HEIGHT: Final[int] = 720

FRAME_PER_SECOND: Final[int] = 144

LINE_WIDTH: Final[int] = 10  # px


def init_vars(source: dict) -> None:
    """Init vars for game."""
    global SC_WIDTH, SC_HEIGHT

    SC_WIDTH = source["width_window"]
    SC_HEIGHT = source["width_window"]


with open(f"{APP_PATH}/settings.txt") as f, open(f"{APP_PATH}/main_settings.json", "w") as data_file:
    things = ("first_move", "figure_player", "width_window")
    values: list[Any] = []
    for line in f:
        if ":" in line:
            data_line = line[line.index(":") + 1 :].strip().lower()
            values.append(int(data_line) if data_line.isdigit() else data_line)

    try:
        data = dict(zip(things, values, strict=False))
        assert len(data) == LENTH_BOARD
    except AssertionError:
        data = DEFAULT_SETT

    init_vars(data)
    json.dump(data, data_file)

FRAME_RATE = 120

BOARD_COLS = 3
BOARD_ROWS = 3

CIRCLE_RADIUS = int(SC_WIDTH * 0.1)  # 600px -- 10% = 60px
CROSS_WIDTH = int(SC_WIDTH * 0.0417)  # 600px -- 4.17% = 25px default
CIRCLE_WIDTH = int(SC_WIDTH * 0.025)  # 600px -- 2.5% = 15px default
WIN_LINE_WIDTH = CIRCLE_WIDTH

SPACE = int(SC_WIDTH * 0.0917)  # 600px -- 9.17% = 55px default
SQUARE_SIZE = SC_WIDTH // 3  # only 3 cells on the field lol
