from typing import List, Dict


def get_phrases(*, instruments: List[str], list_notes: List[str]) -> Dict:
    if len(instruments) != len(list_notes):
        raise Exception("Deben tener la misma longitud.")
    return {instrument: notes for instrument, notes in zip(instruments, list_notes)}

def get_notes_by_repetition(*, notes: str, note_division: int):
    """Concatena el patrón de `notes`, una cantidad `note_division` veces.
    - Ejemplo: `note_division=4` y `notes='1000101'` -> `'1000101100010110001011000101'`
    """
    return notes * note_division

def get_phrases_by_repetition(*, instruments: List[str], list_notes: List[str], note_division: int):
    """
    Dada una frase de longitud `note_division`, hace el compás
    por repetición de esa frase `note_division` veces.
    """
    phrases = {}
    for instrument, notes in zip(instruments, list_notes):
        phrases[instrument] = get_notes_by_repetition(notes=notes, note_division=note_division)
    return phrases