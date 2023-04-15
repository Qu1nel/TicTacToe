import json
import os

APP_PATH = os.path.dirname(os.path.realpath(__file__))


def init_vars(source: dict) -> None:
    global SC_WIDTH, SC_HEIGHT, GO_FIRST, FIGURE_PLAYER, FIGURE_COMPUTER
    SC_WIDTH = SC_HEIGHT = source['width_window']
    GO_FIRST = source['first_move'].upper()
    fig = source['figure_player']
    FIGURE_PLAYER = (fig, 2 if fig == 'cross' else 1)
    FIGURE_COMPUTER = ('cross' if fig == 'circle' else 'circle', FIGURE_PLAYER[1] % 2 + 1)


DEFAULT_SETT = {'first_move': 'COMPUTER', 'figure_player': 'cross', 'width_window': 600}

SC_WIDTH = None
SC_HEIGHT = None

CAPTION = 'TicTacToe'
GO_FIRST = None  # COMPUTER or PLAYER

FIGURE_PLAYER = None  # ('cross', 2)
FIGURE_COMPUTER = None  # ('circle', 1)

with open(f'{APP_PATH}/settings.txt', 'r') as f, open(f'{APP_PATH}/main_settings.json', 'w') as data_file:
    things = ('first_move', 'figure_player', 'width_window')
    values = []
    for line in f:
        if ':' in line:
            data = line[line.index(':') + 1:].strip().lower()
            values.append(int(data) if data.isdigit() else data)

    try:
        data = dict(zip(things, values))
        assert len(data) == 3
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
LINE_WIDTH = CROSS_WIDTH
WIN_LINE_WIDTH = CIRCLE_WIDTH

SPACE = int(SC_WIDTH * 0.0917)  # 600px -- 9.17% = 55px default
SQUARE_SIZE = SC_WIDTH // 3  # only 3 cells on the field lol
