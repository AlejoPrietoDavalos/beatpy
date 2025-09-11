from typing import Dict, List

from drum_machine.const import path_drum_sounds
from pgstudio.sounds import SoundsPGS

DEFAULT_SAMPLES_NAME = "default"
T_Pattern = Dict[str, List[int]]


class SoundsSamples(SoundsPGS):
    """TODO: Abstraer la parte del audio de pygame."""
    def __init__(self, *, samples_name: str = DEFAULT_SAMPLES_NAME):
        super().__init__()
        self.samples_name = samples_name
        self.path_samples = path_drum_sounds / samples_name
        self._load_samples()

    def _load_samples(self) -> None:
        """Carga los sonidos de la batería."""
        for path_sound in self.path_samples.iterdir():
            # TODO: Hacer con glob.
            sound_id = path_sound.stem
            self.load_sound(sound_id=sound_id, path_sound=path_sound)
