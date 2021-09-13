# --------------
# All graphic components of the game depending on the screen size (Width and Height)
# P.S.(preferably the same value is a multiple of 3)
# --------------
SC_WIDTH = 600
SC_HEIGHT = 600

CAPTION = 'TicTacToe'
GO_FIRST = 'COMPUTER'  # COMPUTER or PLAYER

FIGURE_PLAYER = ('cross', 2)
FIGURE_COMPUTER = ('circle', 1)

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
