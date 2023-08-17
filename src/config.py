from typing import Final

from src.misc import Figure, PlayerID

FIRST_MOVE: Final = PlayerID.COMPUTER  # COMPUTER or PLAYER
PLAYER_FIGURE: Final = Figure.CIRCLE  # CIRCLE or CROSS

CIRCLE_WIDTH: Final = 15
CROSS_WIDTH: Final = 20

LINE_WIDTH: Final = 8
WINNER_LINE_WIDTH: Final = 6

WINDOW_SIZE: Final = 720

CELL_SIZE: Final = WINDOW_SIZE // 3

SPACE_FOR_CROSS = int(CELL_SIZE * 0.8)

CIRCLE_RADIUS: Final = 80

FRAME_PER_SECOND: Final = 144
