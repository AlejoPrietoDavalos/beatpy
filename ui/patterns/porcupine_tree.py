from drum_machine.entities.pattern import DrumPatterns, TInstruments
from drum_machine.phrases import get_phrases


from drum_machine.phrases import get_notes_by_repetition
from drum_machine.entities.pattern import DrumPatterns, DrumPattern, TInstruments

BPM = 90
NOTE_DIVISION = 4


class PorcupineTree:
    @staticmethod
    def the_sound_of_the_muzak():
        return DrumPatterns.from_phrase(
            bpm=BPM,
            note_division=NOTE_DIVISION,
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

    @staticmethod
    def the_sound_of_the_muzak_v2():
        return DrumPatterns.from_phrase(
            bpm=BPM,
            note_division=NOTE_DIVISION,
            phrases={
                TInstruments.hihat_closed.value: "1000" * 7,
                TInstruments.snare.value: get_notes_by_repetition(
                    notes="0000010",
                    note_division=NOTE_DIVISION
                ),
                TInstruments.kick.value: get_notes_by_repetition(
                    notes="1001000",
                    note_division=NOTE_DIVISION
                )
            }
        )
