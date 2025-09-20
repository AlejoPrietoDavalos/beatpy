import pygame as pg

from pgstudio.color import T_Color
from pgstudio.pygame_tools.draw import PyGameDraw
from pgstudio.sprites.base import Drawable


class Rect(Drawable):
    def __init__(self, *, color: T_Color, x: int, y: int, width: int, height: int):
        self.color = color
        self.rect = pg.Rect(x, y, width, height)

    def set_position(self, *, x: int, y: int) -> None:
        self.rect.topleft = (x, y)

    def draw(self, *, surface: pg.Surface) -> None:
        PyGameDraw.rect(surface, self.color, self.rect)
