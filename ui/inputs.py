def get_file_count() -> int:
    num = int(input("Введите число файлов для генерации: "))
    return num


def get_harmony_length() -> int:
    num = int(input("Введите число аккордов в гармонии: "))

    if num <= 1:
        raise ValueError("Гармония начинается с двух аккордов")
    
    return num