from typing import Dict, List
from pathlib import Path

import pygame

DEFAULT_SAMPLES_NAME = "default"
T_Pattern = Dict[str, List[int]]


class SoundsPGS:
    def __init__(self):
        self.sounds: Dict[str, pygame.mixer.Sound] = {}

    def load_sound(self, *, sound_id: str, path_sound: Path):
        if sound_id in self.sounds:
            raise ValueError(f"Duplicated sound_id={sound_id}")
        self.sounds[sound_id] = pygame.mixer.Sound(str(path_sound))

    def play_sound(self, *, sound_id: str) -> None:
        """Reproduce el sonido del instrumento."""
        if sound_id not in self.sounds:
            raise ValueError((
                "El instrumento no se encuentra cargado."
                f"Sonidos cargados: {list(self.sounds.keys())}"
            ))
        self.sounds[sound_id].play()