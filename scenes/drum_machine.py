import logging

import pygame as pg

from drum_machine.entities.pattern import DrumPatterns
from drum_machine.player import DrumMachinePlayer
from pgstudio.scene import SceneBase

logger = logging.getLogger(__name__)


class DrumMachineScene(SceneBase):
    def __init__(self, *, name: str, drum_patterns: DrumPatterns):
        super().__init__(name=name)
        self.player = DrumMachinePlayer(drum_patterns=drum_patterns)
        # self.register_keydown(pg.K_g, lambda: logger.info("Presionaste G"))
        # self.register_mouse(1, lambda e: logger.info(f"Click izquierdo en {e.pos}"))

    def main(self) -> None:
        self.player.update()
