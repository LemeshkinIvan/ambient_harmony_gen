from common.const import INTERVALS, NOTE_TO_MIDI
from dto.chord_midi import ChordMidiDTO
from domain.randomizer import get_random_inversion, random_note, random_interval

# строим основной вид аккорда
def build_base_chord_form(root: str, chord_type: str) -> list[int]:
    root_midi = NOTE_TO_MIDI[root]
    return [root_midi + i for i in INTERVALS[chord_type]]

# строим все обращения заданного аккорда
def build_all_chord_forms(base_form: list[int]) -> list[list[int]]:
    res = []
    res.append(base_form.copy())

    """
        Stages Of Transformations 
        origin [1, 3, 5] -> append(0) [1, 3, 5, 1] -> pop(0) [3, 5, 1]
    """
    for r in range(len(base_form)):
        first = base_form.pop(0)
        base_form.append(first)
        res.append(base_form.copy())

    return res

def build_rand_chord() -> ChordMidiDTO:
    root = random_note()
    chord_type = random_interval()

    base_form = build_base_chord_form(root= root, chord_type= chord_type) 
    forms = build_all_chord_forms(base_form= base_form)
    
    return ChordMidiDTO(name= root + chord_type, forms= forms)


def build_harmony(chord_count: int) -> list[list[int]]:
    result = []
    for i in range(chord_count):
        chord = build_rand_chord()
        result.append(get_random_inversion(chord))
    
    return result
