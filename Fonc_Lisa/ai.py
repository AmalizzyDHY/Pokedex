from pokemon import Pokemon
from traitement_db import traitementDB
import random

pokedex = traitementDB()
possibilite_pkmn = pokedex.copy()

# Fonction pour voir si le pokemon est possible ou non, selon le dernier retour du la dernier proposition
def is_compatible(pokemon, guess, feedback):
    """
    pokemon : Pokemon (candidat possible)
    guess   : Pokemon (pokemon joué au dernier tour)
    feedback: dict (Less / More / True / Nearly)
    """

    # ---------- ID ----------
    if feedback["id"] == "Less" and pokemon.get_id() >= guess.get_id():
        return False
    if feedback["id"] == "More" and pokemon.get_id() <= guess.get_id():
        return False
    if feedback["id"] == "True" and pokemon.get_id() != guess.get_id():
        return False

    # ---------- Name ----------
    if feedback["name"] is True and pokemon.get_name() != guess.get_name():
        return False
    if feedback["name"] is False and pokemon.get_name() == guess.get_name():
        return False

    # ---------- Height ----------
    if feedback["height"] == "Less" and pokemon.get_height() >= guess.get_height():
        return False
    if feedback["height"] == "More" and pokemon.get_height() <= guess.get_height():
        return False
    if feedback["height"] == "True" and pokemon.get_height() != guess.get_height():
        return False

    # ---------- Weight ----------
    if feedback["weight"] == "Less" and pokemon.get_weight() >= guess.get_weight():
        return False
    if feedback["weight"] == "More" and pokemon.get_weight() <= guess.get_weight():
        return False
    if feedback["weight"] == "True" and pokemon.get_weight() != guess.get_weight():
        return False

    # ---------- Generation ----------
    if feedback["gen"] == "Less" and pokemon.get_gen() >= guess.get_gen():
        return False
    if feedback["gen"] == "More" and pokemon.get_gen() <= guess.get_gen():
        return False
    if feedback["gen"] == "True" and pokemon.get_gen() != guess.get_gen():
        return False

    # ---------- Type 1 ----------
    if feedback["type1"] == "True" and pokemon.get_type1() != guess.get_type1():
        return False
    if feedback["type1"] == "False" and guess.get_type1() in (pokemon.get_type1(), pokemon.get_type2()):
        return False
    if feedback["type1"] == "Nearly" and guess.get_type1() != pokemon.get_type2():
        return False

    # ---------- Type 2 ----------
    if feedback["type2"] == "True" and pokemon.get_type2() != guess.get_type2():
        return False
    if feedback["type2"] == "False" and guess.get_type2() in (pokemon.get_type1(), pokemon.get_type2()):
        return False
    if feedback["type2"] == "Nearly" and guess.get_type2() != pokemon.get_type1():
        return False

    return True


# On met à jour la liste de pokemon possible selon la dernière propostion faite
def update_possible_pokemons(last_guess, feedback):
    global possibilite_pkmn

    possibilite_pkmn = [
        p for p in possibilite_pkmn
        if is_compatible(p, last_guess, feedback)
    ]

# On choisis la prochaine proposition à partir des pokemons encore proposable
def choose_next_guess():
    choice = random.choice(possibilite_pkmn)
    return choice.get_id()
