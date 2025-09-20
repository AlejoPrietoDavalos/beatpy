from abc import ABC, abstractmethod

import pygame as pg

from pgstudio.color import T_Color


class PyGameDraw:
    @staticmethod
    def rect(surface: pg.Surface, color: T_Color, rect: pg.Rect) -> None:
        pg.draw.rect(surface, color, rect)

    @staticmethod
    def circle(
            *,
            surface: pg.Surface,
            color: T_Color,
            x: int,
            y: int,
            radius: int
    ) -> None:
        pg.draw.circle(surface, color, (x, y), radius)



class Drawable(ABC):
    @abstractmethod
    def set_position(self, *, x: int, y: int) -> None:
        """Mueve el objeto a la posición (x, y)."""
        ...

    @abstractmethod
    def draw(self, *, surface: pg.Surface) -> None:
        """Dibuja el objeto en la `surface`."""
        ...


class Rect(Drawable):
    def __init__(self, *, color: T_Color, x: int, y: int, width: int, height: int):
        self.color = color
        self.rect = pg.Rect(x, y, width, height)

    def set_position(self, *, x: int, y: int) -> None:
        self.rect.topleft = (x, y)

    def draw(self, *, surface: pg.Surface) -> None:
        PyGameDraw.rect(surface, self.color, self.rect)


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
