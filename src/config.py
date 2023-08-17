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

FIRST_MOVE: Final = PlayerID.COMPUTER  # COMPUTER or PLAYER
PLAYER_FIGURE: Final = Figure.CIRCLE  # CIRCLE or CROSS

WINDOW_SIZE: Final = 720  # px

FRAME_PER_SECOND: Final = 144

LINE_WIDTH: Final = 8  # px
WINNER_LINE_WIDTH: Final = 6  # px
CELL_SIZE: Final = WINDOW_SIZE // 3

CIRCLE_RADIUS: Final = 80  # px

CIRCLE_WIDTH: Final = 15  # px
CROSS_WIDTH: Final = 25  # px


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

SPACE = int(SC_WIDTH * 0.0917)  # 600px -- 9.17% = 55px default
SQUARE_SIZE = SC_WIDTH // 3  # only 3 cells on the field lol
