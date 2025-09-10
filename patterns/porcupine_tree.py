from drum_machine.entities.pattern import DrumPatterns, TInstruments
from drum_machine.phrases import get_phrases


class PorcupineTree:
    @staticmethod
    def the_sound_of_the_muzak():
        return DrumPatterns.from_phrase(
            bpm=90,
            note_division=4,
            phrases=get_phrases(
                instruments=[
                    TInstruments.hihat_closed.value,
                    TInstruments.snare.value,
                    TInstruments.kick.value
                ],
                list_notes=[
                    "1000" + "1000" + "1000" + "1000" + "1000" + "1000" + "1000",
                    "0000" + "0100" + "0000" + "1000" + "0001" + "0000" + "0010",
                    "1001" + "0001" + "0010" + "0010" + "0100" + "0100" + "1000",
                ]
            )
        )
