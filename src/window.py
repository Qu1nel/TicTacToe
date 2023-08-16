import pygame as pg

from src.misc import Singleton


class Window(metaclass=Singleton):
    """Base window class.

    Attributes:
        width: Window width.
        height: Window height.
        screen: Window surface (can draw sprites).
        clock: Frames counting cycles.
        fps: FPS indicator.

    """

    width: int
    height: int
    screen: pg.SurfaceType
    clock: pg.time.Clock
    fps: int

    def __init__(self, width: int, height: int, fps: int) -> None:
        self.width = width
        self.height = height

        self.screen = pg.display.set_mode((width, height))

        self.clock = pg.time.Clock()
        self.fps = fps
