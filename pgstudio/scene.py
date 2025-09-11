from __future__ import annotations
from typing import TypeVar, Callable, Dict, Any, Optional
from abc import ABC, abstractmethod
import logging

import pygame as pg

from pgstudio.color import BLACK
from pgstudio._core.window import WindowPGS
from pgstudio._core.clock import ClockPGS

logger = logging.getLogger(__name__)


T_SceneBase = TypeVar("SceneBase", bound="SceneBase")


class _SceneBase(ABC):
    def __init__(self, *, name: str):
        self.name = name
        self.is_running = False
        # Handlers para eventos de pygame (por tipo de evento)
        self.events: Dict[int, Callable[[], Any]] = {}

        # Handlers para teclas (por código de tecla)
        self.keydown_events: Dict[int, Callable[[], Any]] = {}
        self.keyup_events: Dict[int, Callable[[], Any]] = {}

        # Handlers para clicks de mouse (por botón: 1=izq, 2=medio, 3=der)
        self.mouse_events: Dict[int, Callable[[pg.event.Event], Any]] = {}
        self.register_keydown(pg.K_ESCAPE, self.set_is_not_running)

    def __enter__(self) -> None:
        """ Se ejecuta al `entrar` en la escena. """
        logger.info(f"[Start Scene] {self.name}")
        self.set_is_running()

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """ Se ejecuta al `salir` de la escena."""
        logger.info(f"[Exit Scene] {self.name}")

    def set_is_running(self) -> None:
        self.is_running = True

    def set_is_not_running(self) -> None:
        logger.info("Set is_running=False")
        self.is_running = False

    def register_keydown(self, key: int, handler: Callable[[], Any]) -> None:
        """Registrar acción para cuando se presione una tecla."""
        self.keydown_events[key] = handler

    def register_mouse(self, button: int, handler: Callable[[pg.event.Event], Any]) -> None:
        """Registrar acción para click de mouse."""
        self.mouse_events[button] = handler


class SceneBase(_SceneBase):
    def __init__(self, name: str):
        super().__init__(name=name)

    def run_fill(self) -> None:
        """ Como rellenar el fondo. Por default se pinta de negro.
        - TODO: Quizás se podría crear un objeto `Background` que
        se encargue del fondo de la escena."""
        ...

    def run_events(self) -> None:
        for event in pg.event.get():
            # Primero eventos genéricos como QUIT
            fn_event = self.events.get(event.type)
            if fn_event:
                fn_event()

            # Eventos de teclado
            if event.type == pg.KEYDOWN:
                fn_keydown = self.keydown_events.get(event.key)
                if fn_keydown:
                    fn_keydown()

            # Eventos de mouse
            if event.type == pg.MOUSEBUTTONDOWN:
                fn_mouse = self.mouse_events.get(event.button)
                if fn_mouse:
                    fn_mouse(event)

    def run_scene(self, window: WindowPGS, clock: ClockPGS) -> Optional[str]:
        """ Loop principal de la escena."""
        next_scene_name = None  # TODO: Como cambiar entre scenes?
        with self:
            while self.is_running:
                window.fill(color=BLACK)
                self.run_fill()
                self.run_events()
                self.main()
                clock.refresh()
        return next_scene_name

    @abstractmethod
    def main(self) -> None:
        ...
