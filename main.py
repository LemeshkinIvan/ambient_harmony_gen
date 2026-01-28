from domain.harmony_builder import build_harmony
from domain.generate_midi import generate_midi
from infrastructure.save_midi import save_as_file
from ui.inputs import get_file_count, get_harmony_length

def main():
    try:
        file_count = get_file_count()
        length = get_harmony_length()

        for i in range(file_count):
            harmony = build_harmony(chord_count=length)
            midi = generate_midi(harmony=harmony)
            save_as_file(fileName= f"track {i}.mid", file= midi)
            
        print(f"Все файлы были успешно созданы и добавлены в папку output!")
    except Exception as e:
        print(f"Неожиданная ошибка {e}")
    
if __name__=="__main__":
    main()