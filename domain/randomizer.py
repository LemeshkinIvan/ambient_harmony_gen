import random
from dto.chord_midi import ChordMidiDTO
from common.const import *

def random_note() -> str:
    return random.choice(list(NOTE_TO_MIDI.keys()))

def random_interval() -> str:
    return random.choice(list(INTERVALS.keys()))

def get_random_inversion(chord: ChordMidiDTO) -> list[int]:
   return random.choice(chord.all_forms)