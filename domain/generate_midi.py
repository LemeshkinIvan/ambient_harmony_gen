from mido import MidiFile, MidiTrack, Message, bpm2tempo, MetaMessage
from common.const import PPQ, DEFAULT_TEMPO

def generate_midi(harmony: list[list[int]]) -> MidiFile:
        mid = MidiFile(ticks_per_beat=PPQ) 
        track = MidiTrack() 
        mid.tracks.append(track)

        track.append(MetaMessage('set_tempo', tempo=bpm2tempo(DEFAULT_TEMPO)))
        duration_chord = PPQ * 3 # 3 целых такта

        for chord in harmony:
            for note in chord:
                track.append(Message('note_on', note=note, velocity=64, time=0))
            
            for i, note in enumerate(chord):
                track.append(Message('note_off', note=note, velocity=64, time=duration_chord if i == 0 else 0))

        return mid