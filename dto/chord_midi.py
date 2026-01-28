class ChordMidiDTO:
    def __init__(self, name: str, forms: list[list[int]]):
        self.name = name
        self.all_forms = forms

    def __str__(self) -> str:
        return (
            f"Name: {self.name}\n"
            f"Inversion:{self.all_forms}"
        )
