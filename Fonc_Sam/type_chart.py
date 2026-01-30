from pokemon import Pokemon

# Liste officielle des types Pokémon
TYPES = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice",
    "Fighting", "Poison", "Ground", "Flying", "Psychic", "Bug",
    "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"
]



# Table des multiplicateurs (initialisée à 1.0 partout)
TYPE_CHART = {atk: {def_: 1.0 for def_ in TYPES} for atk in TYPES}


# Function helper to set multipliers
def set_mult(atk_type: str, defenders: list, mult: float) -> None:
    """
    Définit le multiplicateur d'efficacité pour un type attaquant
    contre une liste de types défenseurs.
    """
    for d in defenders:
        TYPE_CHART[atk_type][d] = float(mult)


# Règles d'efficacité
set_mult("Fire", ["Grass", "Ice", "Bug", "Steel"], 2.0)
set_mult("Fire", ["Fire", "Water", "Rock", "Dragon"], 0.5)

set_mult("Water", ["Fire", "Ground", "Rock"], 2.0)
set_mult("Water", ["Water", "Grass", "Dragon"], 0.5)

set_mult("Electric", ["Water", "Flying"], 2.0)
set_mult("Electric", ["Electric", "Grass", "Dragon"], 0.5)
set_mult("Electric", ["Ground"], 0.0)

# Prérequis : TYPES + TYPE_CHART initialisé à 1.0 + set_mult déjà défini

# Normal
set_mult("Normal", ["Rock", "Steel"], 0.5)
set_mult("Normal", ["Ghost"], 0.0)

# Fire
set_mult("Fire", ["Grass", "Ice", "Bug", "Steel"], 2.0)
set_mult("Fire", ["Fire", "Water", "Rock", "Dragon"], 0.5)

# Water
set_mult("Water", ["Fire", "Ground", "Rock"], 2.0)
set_mult("Water", ["Water", "Grass", "Dragon"], 0.5)

# Electric
set_mult("Electric", ["Water", "Flying"], 2.0)
set_mult("Electric", ["Electric", "Grass", "Dragon"], 0.5)
set_mult("Electric", ["Ground"], 0.0)

# Grass
set_mult("Grass", ["Water", "Ground", "Rock"], 2.0)
set_mult("Grass", ["Fire", "Grass", "Poison", "Flying", "Bug", "Dragon", "Steel"], 0.5)

# Ice
set_mult("Ice", ["Grass", "Ground", "Flying", "Dragon"], 2.0)
set_mult("Ice", ["Fire", "Water", "Ice", "Steel"], 0.5)

# Fighting
set_mult("Fighting", ["Normal", "Ice", "Rock", "Dark", "Steel"], 2.0)
set_mult("Fighting", ["Poison", "Flying", "Psychic", "Bug", "Fairy"], 0.5)
set_mult("Fighting", ["Ghost"], 0.0)

# Poison
set_mult("Poison", ["Grass", "Fairy"], 2.0)
set_mult("Poison", ["Poison", "Ground", "Rock", "Ghost"], 0.5)
set_mult("Poison", ["Steel"], 0.0)

# Ground
set_mult("Ground", ["Fire", "Electric", "Poison", "Rock", "Steel"], 2.0)
set_mult("Ground", ["Grass", "Bug"], 0.5)
set_mult("Ground", ["Flying"], 0.0)

# Flying
set_mult("Flying", ["Grass", "Fighting", "Bug"], 2.0)
set_mult("Flying", ["Electric", "Rock", "Steel"], 0.5)

# Psychic
set_mult("Psychic", ["Fighting", "Poison"], 2.0)
set_mult("Psychic", ["Psychic", "Steel"], 0.5)
set_mult("Psychic", ["Dark"], 0.0)

# Bug
set_mult("Bug", ["Grass", "Psychic", "Dark"], 2.0)
set_mult("Bug", ["Fire", "Fighting", "Poison", "Flying", "Ghost", "Steel", "Fairy"], 0.5)

# Rock
set_mult("Rock", ["Fire", "Ice", "Flying", "Bug"], 2.0)
set_mult("Rock", ["Fighting", "Ground", "Steel"], 0.5)

# Ghost
set_mult("Ghost", ["Psychic", "Ghost"], 2.0)
set_mult("Ghost", ["Dark"], 0.5)
set_mult("Ghost", ["Normal"], 0.0)

# Dragon
set_mult("Dragon", ["Dragon"], 2.0)
set_mult("Dragon", ["Steel"], 0.5)
set_mult("Dragon", ["Fairy"], 0.0)

# Dark
set_mult("Dark", ["Psychic", "Ghost"], 2.0)
set_mult("Dark", ["Fighting", "Dark", "Fairy"], 0.5)

# Steel
set_mult("Steel", ["Ice", "Rock", "Fairy"], 2.0)
set_mult("Steel", ["Fire", "Water", "Electric", "Steel"], 0.5)

# Fairy
set_mult("Fairy", ["Fighting", "Dragon", "Dark"], 2.0)
set_mult("Fairy", ["Fire", "Poison", "Steel"], 0.5)




def multiplier(attack_type: str, defender: Pokemon) -> float:
    """
    Calcule le multiplicateur de dégâts d'un type d'attaque
    contre un Pokémon défenseur (mono ou double type).
    """
    mult = 1.0

    # Type 1 (toujours présent)
    mult *= TYPE_CHART[attack_type][defender.type1]

    # Type 2 (optionnel)
    if defender.type2 is not None:
        mult *= TYPE_CHART[attack_type][defender.type2]

    return mult



