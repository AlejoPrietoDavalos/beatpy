import logging
import time

from drum_machine.entities.pattern import DrumPatterns
from drum_machine.samples import SoundsSamples

logger = logging.getLogger(__name__)


def get_time_now() -> float:
    """Utilizar para mayor precisión."""
    return time.perf_counter()


class DrumMachinePlayer:
    """Reproduce los sonidos de batería dado un `DrumPatterns`."""

    def __init__(self, *, drum_patterns: DrumPatterns):
        self.drum_patterns = drum_patterns
        self.samples = SoundsSamples()
        self.step = 0
        self.time_last = get_time_now()

    def play_step(self) -> None:
        pattern_index = self.step // self.drum_patterns.note_division
        step_in_pattern = self.step % self.drum_patterns.note_division

        drum_pattern = self.drum_patterns.patterns[pattern_index]
        instrument_hits = drum_pattern.get_instrument_hits(step=step_in_pattern)
        logger.info(f"Step={self.step} | Pattern={pattern_index} | Hits: {instrument_hits}")

        for instrument_hit in instrument_hits:
            self.samples.play_sound(sound_id=instrument_hit)

    def next_step(self) -> None:
        """Avanza al siguiente step dentro del compás."""
        total_steps = len(self.drum_patterns.patterns) * self.drum_patterns.note_division
        self.step = (self.step + 1) % total_steps

    def update(self) -> None:
        """Chequea si debe avanzar un step y reproducirlo."""
        time_now = get_time_now()
        if time_now - self.time_last >= self.drum_patterns.step_duration:
            self.play_step()
            self.next_step()
            self.time_last = time_now


# visualizar division de un compas de N/M en N hits con M repeticiones.
