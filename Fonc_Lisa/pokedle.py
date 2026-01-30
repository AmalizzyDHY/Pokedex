from pokemon import Pokemon
from traitement_db import traitementDB
import random

def game():

    pokedex = traitementDB()
    win = 0

    # choix du pokemon "mystère"
    n_pkmn_mystere = random.randint(1, 1025) # On choisis un numéro entre 1 et 1025, ce qui choisis le numéro du pokemon "mystère"
    pokedex[n_pkmn_mystere].show()

    while not win:
        # L'utilisateur choisis un pokemon, pour deviner le pokemon mystère
        n_pkmn_guest = int(input("Try : "))
        # print(pokedex[n_pkmn_guest])

        if n_pkmn_guest == n_pkmn_mystere :
            print("Tu as gagner ! C'était bien " + str(pokedex[n_pkmn_mystere].get_name()))
            win = 1
        else :
            print("Essaie encore")
            
            # Indice pour savoir si on augmente ou descent
            if(pokedex[n_pkmn_guest].get_id() <= pokedex[n_pkmn_mystere].get_id()):
                indice_id = "More"
            else:
                indice_id = "Less"

            # Indice pour savoir le type1 du pokemon
            if(pokedex[n_pkmn_guest].get_type1() == pokedex[n_pkmn_mystere].get_type1()):
                indice_type1 = "True"
            else:
                if(pokedex[n_pkmn_guest].get_type1() == pokedex[n_pkmn_mystere].get_type2()):
                    indice_type1 = "Nearly"
                else:
                    indice_type1 = "False"

            # Indice pour savoir le type2 du pokemon
            if(pokedex[n_pkmn_guest].get_type2() == pokedex[n_pkmn_mystere].get_type2()):
                indice_type2 = "True"
            else:
                if(pokedex[n_pkmn_guest].get_type2() == pokedex[n_pkmn_mystere].get_type1()):
                    indice_type2 = "Nearly"
                else:
                    indice_type2 = "False"

            # Indice pour savoir le height du pokemon
            if(pokedex[n_pkmn_guest].get_height() <= pokedex[n_pkmn_mystere].get_height()):
                indice_height = "More"
            else:
                indice_height = "Less"
            
            # Indice pour savoir le weight du pokemon
            if(pokedex[n_pkmn_guest].get_weight() <= pokedex[n_pkmn_mystere].get_weight()):
                indice_weight = "More"
            else:
                indice_weight = "Less"

            # Indice pour savoir si on augmente ou descent pour la generation
            if(pokedex[n_pkmn_guest].get_gen() <= pokedex[n_pkmn_mystere].get_gen()):
                indice_gen = "More"
            else:
                indice_gen = "Less"

            print("ID               : " + str(pokedex[n_pkmn_guest].get_id()) + " - " + indice_id)
            print("Name             : " + str(pokedex[n_pkmn_guest].get_name()) + " - " + str(pokedex[n_pkmn_guest].get_name() == pokedex[n_pkmn_mystere].get_name()))
            print("Type 1           : " + str(pokedex[n_pkmn_guest].get_type1()) + " - " + indice_type1)
            print("Type 2           : " + str(pokedex[n_pkmn_guest].get_type2()) + " - " + indice_type2)
            print("Height Meters    : " + str(pokedex[n_pkmn_guest].get_height()) + " - " + indice_height)
            print("Weight Kilograms : " + str(pokedex[n_pkmn_guest].get_weight()) + " - " + indice_weight)
            print("Generation       : " + str(pokedex[n_pkmn_guest].get_gen()) + " - " + indice_gen)
        