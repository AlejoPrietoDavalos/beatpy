from typing import Callable, Optional
from abc import ABC, abstractmethod
import logging

import pygame as pg

logger = logging.getLogger(__name__)


class Drawable(ABC):
    def __init__(
            self,
            *,
            on_click: Optional[Callable[[], None]] = None
    ):
        self._on_click = on_click

    @abstractmethod
    def set_position(self, *, x: int, y: int) -> None:
        """Mueve el objeto a la posición (x, y)."""
        ...

    @abstractmethod
    def draw(self, *, surface: pg.Surface) -> None:
        """Dibuja el objeto en la `surface`."""
        ...

    @abstractmethod
    def is_mouse_up(self, *, mouse_x: int, mouse_y: int) -> bool:
        """Debe retornar un booleano que determine si el mouse en encuentra encima o no."""
        ...

    def click(self, *, mouse_x: int, mouse_y: int) -> None:
        if not self.is_mouse_up(mouse_x=mouse_x, mouse_y=mouse_y):
            return None

        if self._on_click is not None:
            self._on_click()
        else:
            logger.warning((
                "Se hizo click pero no se asignó una "
                f"función a ejecutar `on_click`"
            ))
