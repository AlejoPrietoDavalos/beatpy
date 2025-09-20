import pygame as pg

from pgstudio.color import T_Color


class PyGameDraw:
    """Dibuja un elemento en la UI."""
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
