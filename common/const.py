# C/Am tone
NOTE_TO_MIDI = {
    "C": 60,
    "D": 62,
    "E": 64,
    "F": 65,
    "G": 67,
    "A": 69,
    "B": 71,
}

INTERVALS = {
    "maj": [0, 4, 7],
    #"min": [0, 3, 7],
    "sus2":   [0, 2, 7],
    "sus4":   [0, 5, 7],
    "add6":   [0, 4, 7, 9],
    "add9":   [0, 4, 7, 14],
    "add11":   [0, 4, 7, 9, 16],
    "add13":   [0, 4, 7, 11, 18],
}

PPQ = 1920 # whole note
DEFAULT_TEMPO = 90