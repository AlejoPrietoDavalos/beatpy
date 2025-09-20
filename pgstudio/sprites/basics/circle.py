import pygame as pg

from pgstudio.color import T_Color
from pgstudio.pygame_tools.draw import PyGameDraw
from pgstudio.sprites.base import Drawable


class Circle(Drawable):
    def __init__(self, *, color: T_Color, x: int, y: int, radius: int):
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius

    def set_position(self, *, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def draw(self, *, surface: pg.Surface) -> None:
        PyGameDraw.circle(surface=surface, color=self.color, x=self.x, y=self.y, radius=self.radius)
