from typing import List
import logging

import pygame as pg

from drum_machine.entities.pattern import DrumPatterns
from drum_machine.player import DrumMachinePlayer
from pgstudio.scene import SceneBase
from pgstudio.core.sprites.base import Drawable, Rect, Circle

logger = logging.getLogger(__name__)


class DrumMachineScene(SceneBase):
    def __init__(self, *, name: str, drum_patterns: DrumPatterns):
        super().__init__(name=name)
        self.player = DrumMachinePlayer(drum_patterns=drum_patterns)
        self.player.drum_patterns.patterns
        self.COLOR_BACKGROUND = (36, 6, 97)
        self.drawables: List[Drawable] = [
            Rect(color=(255, 0, 0), x=100, y=200, width=50, height=50),
            Circle(color=self.COLOR_BACKGROUND, x=200, y=200, radius=30),
        ]

    def run_fill(self) -> None:
        super().run_fill()
        surface = pg.display.get_surface()
        if surface:
            for drawable in self.drawables:
                drawable.draw(surface=surface)

    def main(self) -> None:
        self.player.update()
