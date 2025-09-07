import time
from drum_machine.entities.pattern import DrumPattern
from drum_machine.samples import Samples


class DrumMachinePlayer:
    """Reproduce un DrumPattern usando los samples cargados."""

    def __init__(self, pattern: DrumPattern):
        self.pattern = pattern
        self.samples = Samples()
        self.step = 0
        self.last_time = time.time()

    @property
    def step_duration(self) -> float:
        """Duración de cada step en segundos según BPM y división de nota."""
        return 60 / self.pattern.bpm / self.pattern.note_division

    def update(self) -> None:
        """Chequea si debe avanzar un step y reproducirlo."""
        now = time.time()
        if now - self.last_time >= self.step_duration:
            self.play_step()
            self.step = (self.step + 1) % self.pattern.steps_total
            self.last_time = now

    def play_step(self) -> None:
        """Ejecuta los samples del step actual."""
        for instrument, inst_pattern in self.pattern.instruments.items():
            if inst_pattern.sequence[self.step % len(inst_pattern.sequence)] == 1:
                self.samples.play_instrument(instrument)
