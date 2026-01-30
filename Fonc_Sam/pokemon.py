class Pokemon:
    """
    Représente un Pokémon avec un ou deux types.
    """

    def __init__(self, name: str, type1: str, type2: str = None):
        self.name = name
        self.type1 = type1
        # Si le type2 vaut "None" (string), on le convertit en vrai None
        self.type2 = None if type2 == "None" else type2

    def describe(self) -> None:
        if self.type2:
            print(f"{self.name} is a {self.type1}/{self.type2} Pokémon.")
        else:
            print(f"{self.name} is a {self.type1}-type Pokémon.")
