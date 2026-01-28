import os
from mido import MidiFile

def save_as_file(fileName: str, file: MidiFile) -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)

    folder_path = os.path.join(parent_dir, "output")
    os.makedirs(folder_path, exist_ok=True)

    full_path = os.path.join(folder_path, fileName)
    file.save(full_path)