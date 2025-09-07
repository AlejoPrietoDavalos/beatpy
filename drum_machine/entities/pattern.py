from typing import Dict, List, Optional
from functools import cached_property
import logging

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)
DEFAULT_BPM = 120
DEFAULT_NOTE_DIVISION = 4


class PatternInstrument(BaseModel):
    name: str
    sequence: List[int] = Field(min_items=1)
    intensity: Optional[List[int]] = None   # FIXME: Para cambiar la intensidad del golpe.


class DrumPattern(BaseModel):
    bpm: int = DEFAULT_BPM
    note_division: int = DEFAULT_NOTE_DIVISION
    instruments: Dict[str, PatternInstrument]

    @cached_property
    def steps_total(self) -> int:
        """Número total de steps del patrón (máx longitud entre instrumentos)."""
        logger.warning("--> Deberian tener todos la misma longitud.")
        return max(len(inst.sequence) for inst in self.instruments.values())