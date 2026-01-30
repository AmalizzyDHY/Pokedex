from pokemon import Pokemon
from traitement_db import traitementDB
from ai import choose_next_guess, update_possible_pokemons, restart_game
import random

def game_solo():

    pokedex = traitementDB()
    win = 0

    # choix du pokemon "mystère"
    n_pkmn_mystere = random.randint(1, 1025) # On choisis un numéro entre 1 et 1025, ce qui choisis le numéro du pokemon "mystère"
    print("Pokemon Mystère")
    pokedex[n_pkmn_mystere].show()
    print("\n")

    while not win:
        # L'utilisateur choisis un pokemon, pour deviner le pokemon mystère
        n_pkmn_guest = int(input("Try : "))
        # print(pokedex[n_pkmn_guest])

        if n_pkmn_guest == n_pkmn_mystere :
            print("You win ! It was : " + str(pokedex[n_pkmn_mystere].get_name()) + "\n")
            win = 1
        else :
            print("Sorry...")
            
            if ( n_pkmn_guest <= 1025 ):
                if ( n_pkmn_guest > 0 ):
                    # Indice pour savoir si on augmente ou descent
                    if(pokedex[n_pkmn_guest].get_id() == pokedex[n_pkmn_mystere].get_id()):
                        indice_id = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_id() <= pokedex[n_pkmn_mystere].get_id()):
                            indice_id = "More"
                        else:
                            indice_id = "Less"

                    # Indice pour connaitre le nom du pokemon
                    indice_name = pokedex[n_pkmn_guest].get_name() == pokedex[n_pkmn_mystere].get_name()

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
                    if(pokedex[n_pkmn_guest].get_height() == pokedex[n_pkmn_mystere].get_height()):
                        indice_height = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_height() <= pokedex[n_pkmn_mystere].get_height()):
                            indice_height = "More"
                        else:
                            indice_height = "Less"
                    
                    # Indice pour savoir le weight du pokemon
                    if(pokedex[n_pkmn_guest].get_weight() == pokedex[n_pkmn_mystere].get_weight()):
                        indice_weight = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_weight() <= pokedex[n_pkmn_mystere].get_weight()):
                            indice_weight = "More"
                        else:
                            indice_weight = "Less"

                    # Indice pour savoir si on augmente ou descent pour la generation
                    if(pokedex[n_pkmn_guest].get_gen() == pokedex[n_pkmn_mystere].get_gen()):
                        indice_gen = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_gen() <= pokedex[n_pkmn_mystere].get_gen()):
                            indice_gen = "More"
                        else:
                            indice_gen = "Less"

                    print("ID               : " + str(pokedex[n_pkmn_guest].get_id()) + " - " + indice_id)
                    print("Name             : " + str(pokedex[n_pkmn_guest].get_name()) + " - " + str(indice_name))
                    print("Type 1           : " + str(pokedex[n_pkmn_guest].get_type1()) + " - " + indice_type1)
                    print("Type 2           : " + str(pokedex[n_pkmn_guest].get_type2()) + " - " + indice_type2)
                    print("Height Meters    : " + str(pokedex[n_pkmn_guest].get_height()) + " - " + indice_height)
                    print("Weight Kilograms : " + str(pokedex[n_pkmn_guest].get_weight()) + " - " + indice_weight)
                    print("Generation       : " + str(pokedex[n_pkmn_guest].get_gen()) + " - " + indice_gen)
                    print("\n")
                else:
                    print("ID of Pokemon start at 1 !\n")
            else:
                print("It's not an ID of Pokemon !\n")

def game_ia():

    pokedex = traitementDB()
    win = 0

    # choix du pokemon "mystère"
    n_pkmn_mystere = random.randint(1, 1025) # On choisis un numéro entre 1 et 1025, ce qui choisis le numéro du pokemon "mystère"
    print("Pokemon Mystère")
    pokedex[n_pkmn_mystere].show()
    print("\n")

    # On fait ça pour remettre à zéro la liste de possibilité
    restart_game()

    while not win:
        # L'IA choisis un pokemon, pour deviner le pokemon mystère
        n_pkmn_guest = int(choose_next_guess())
        print("Try : " + str(n_pkmn_guest))
        # print(pokedex[n_pkmn_guest])

        if n_pkmn_guest == n_pkmn_mystere :
            print("You win ! It was : " + str(pokedex[n_pkmn_mystere].get_name()) + "\n")
            win = 1
        else :
            print("Sorry... Try again !")
            
            # Indice pour savoir si on augmente ou descent
            if(pokedex[n_pkmn_guest].get_id() == pokedex[n_pkmn_mystere].get_id()):
                indice_id = "True"
            else:
                if(pokedex[n_pkmn_guest].get_id() <= pokedex[n_pkmn_mystere].get_id()):
                    indice_id = "More"
                else:
                    indice_id = "Less"

            # Indice pour connaitre le nom du pokemon
            indice_name = pokedex[n_pkmn_guest].get_name() == pokedex[n_pkmn_mystere].get_name()

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
            if(pokedex[n_pkmn_guest].get_height() == pokedex[n_pkmn_mystere].get_height()):
                indice_height = "True"
            else:
                if(pokedex[n_pkmn_guest].get_height() <= pokedex[n_pkmn_mystere].get_height()):
                    indice_height = "More"
                else:
                    indice_height = "Less"
            
            # Indice pour savoir le weight du pokemon
            if(pokedex[n_pkmn_guest].get_weight() == pokedex[n_pkmn_mystere].get_weight()):
                indice_weight = "True"
            else:
                if(pokedex[n_pkmn_guest].get_weight() <= pokedex[n_pkmn_mystere].get_weight()):
                    indice_weight = "More"
                else:
                    indice_weight = "Less"

            # Indice pour savoir si on augmente ou descent pour la generation
            if(pokedex[n_pkmn_guest].get_gen() == pokedex[n_pkmn_mystere].get_gen()):
                indice_gen = "True"
            else:
                if(pokedex[n_pkmn_guest].get_gen() <= pokedex[n_pkmn_mystere].get_gen()):
                    indice_gen = "More"
                else:
                    indice_gen = "Less"

            feedback = {}
            feedback["id"] = indice_id
            feedback["name"] = indice_name
            feedback["type1"] = indice_type1
            feedback["type2"] = indice_type2
            feedback["height"] = indice_height
            feedback["weight"] = indice_weight
            feedback["gen"] = indice_gen

            print("ID               : " + str(pokedex[n_pkmn_guest].get_id()) + " - " + indice_id)
            print("Name             : " + str(pokedex[n_pkmn_guest].get_name()) + " - " + str(indice_name))
            print("Type 1           : " + str(pokedex[n_pkmn_guest].get_type1()) + " - " + indice_type1)
            print("Type 2           : " + str(pokedex[n_pkmn_guest].get_type2()) + " - " + indice_type2)
            print("Height Meters    : " + str(pokedex[n_pkmn_guest].get_height()) + " - " + indice_height)
            print("Weight Kilograms : " + str(pokedex[n_pkmn_guest].get_weight()) + " - " + indice_weight)
            print("Generation       : " + str(pokedex[n_pkmn_guest].get_gen()) + " - " + indice_gen)
            print("\n")

            update_possible_pokemons(pokedex[n_pkmn_guest], feedback)

def game_1v1():

    pokedex = traitementDB()
    win = 0
    play = 0
    # choix du pokemon "mystère"
    n_pkmn_mystere = random.randint(1, 1025) # On choisis un numéro entre 1 et 1025, ce qui choisis le numéro du pokemon "mystère"
    print("Pokemon Mystère")
    pokedex[n_pkmn_mystere].show()
    print("\n")

    while not win:

        print("Turn Player " + str((play%2)+1))
        # L'utilisateur choisis un pokemon, pour deviner le pokemon mystère
        n_pkmn_guest = int(input("Try : "))
        # print(pokedex[n_pkmn_guest])

        if n_pkmn_guest == n_pkmn_mystere :
            print("You win ! It was : " + str(pokedex[n_pkmn_mystere].get_name()) + "\n")
            print("Player " + str((play%2)+1) + " win !")
            win = 1
        else :
            print("Sorry...")
            
            if ( n_pkmn_guest <= 1025 ):
                if ( n_pkmn_guest > 0 ):
                    # Indice pour savoir si on augmente ou descent
                    if(pokedex[n_pkmn_guest].get_id() == pokedex[n_pkmn_mystere].get_id()):
                        indice_id = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_id() <= pokedex[n_pkmn_mystere].get_id()):
                            indice_id = "More"
                        else:
                            indice_id = "Less"

                    # Indice pour connaitre le nom du pokemon
                    indice_name = pokedex[n_pkmn_guest].get_name() == pokedex[n_pkmn_mystere].get_name()

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
                    if(pokedex[n_pkmn_guest].get_height() == pokedex[n_pkmn_mystere].get_height()):
                        indice_height = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_height() <= pokedex[n_pkmn_mystere].get_height()):
                            indice_height = "More"
                        else:
                            indice_height = "Less"
                    
                    # Indice pour savoir le weight du pokemon
                    if(pokedex[n_pkmn_guest].get_weight() == pokedex[n_pkmn_mystere].get_weight()):
                        indice_weight = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_weight() <= pokedex[n_pkmn_mystere].get_weight()):
                            indice_weight = "More"
                        else:
                            indice_weight = "Less"

                    # Indice pour savoir si on augmente ou descent pour la generation
                    if(pokedex[n_pkmn_guest].get_gen() == pokedex[n_pkmn_mystere].get_gen()):
                        indice_gen = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_gen() <= pokedex[n_pkmn_mystere].get_gen()):
                            indice_gen = "More"
                        else:
                            indice_gen = "Less"

                    print("ID               : " + str(pokedex[n_pkmn_guest].get_id()) + " - " + indice_id)
                    print("Name             : " + str(pokedex[n_pkmn_guest].get_name()) + " - " + str(indice_name))
                    print("Type 1           : " + str(pokedex[n_pkmn_guest].get_type1()) + " - " + indice_type1)
                    print("Type 2           : " + str(pokedex[n_pkmn_guest].get_type2()) + " - " + indice_type2)
                    print("Height Meters    : " + str(pokedex[n_pkmn_guest].get_height()) + " - " + indice_height)
                    print("Weight Kilograms : " + str(pokedex[n_pkmn_guest].get_weight()) + " - " + indice_weight)
                    print("Generation       : " + str(pokedex[n_pkmn_guest].get_gen()) + " - " + indice_gen)
                    print("\n")

                    play += 1

                else:
                    print("ID of Pokemon start at 1 !\n")
            else:
                print("It's not an ID of Pokemon !\n")

def game_1via():

    pokedex = traitementDB()
    win = 0
    play = 0
    # choix du pokemon "mystère"
    n_pkmn_mystere = random.randint(1, 1025) # On choisis un numéro entre 1 et 1025, ce qui choisis le numéro du pokemon "mystère"
    print("Pokemon Mystère")
    pokedex[n_pkmn_mystere].show()
    print("\n")

    # On fait ça pour remettre à zéro la liste de possibilité
    restart_game()

    while not win:

        print("Turn Player " + str((play%2)+1))
        # L'utilisateur choisis un pokemon, pour deviner le pokemon mystère
        n_pkmn_guest = int(input("Try : "))
        # print(pokedex[n_pkmn_guest])

        if n_pkmn_guest == n_pkmn_mystere :
            print("You win ! It was : " + str(pokedex[n_pkmn_mystere].get_name()) + "\n")
            print("Player " + str((play%2)+1) + " win !")
            win = 1
        else :
            print("Sorry...")
            
            if ( n_pkmn_guest <= 1025 ):
                if ( n_pkmn_guest > 0 ):
                    # Indice pour savoir si on augmente ou descent
                    if(pokedex[n_pkmn_guest].get_id() == pokedex[n_pkmn_mystere].get_id()):
                        indice_id = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_id() <= pokedex[n_pkmn_mystere].get_id()):
                            indice_id = "More"
                        else:
                            indice_id = "Less"

                    # Indice pour connaitre le nom du pokemon
                    indice_name = pokedex[n_pkmn_guest].get_name() == pokedex[n_pkmn_mystere].get_name()

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
                    if(pokedex[n_pkmn_guest].get_height() == pokedex[n_pkmn_mystere].get_height()):
                        indice_height = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_height() <= pokedex[n_pkmn_mystere].get_height()):
                            indice_height = "More"
                        else:
                            indice_height = "Less"
                    
                    # Indice pour savoir le weight du pokemon
                    if(pokedex[n_pkmn_guest].get_weight() == pokedex[n_pkmn_mystere].get_weight()):
                        indice_weight = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_weight() <= pokedex[n_pkmn_mystere].get_weight()):
                            indice_weight = "More"
                        else:
                            indice_weight = "Less"

                    # Indice pour savoir si on augmente ou descent pour la generation
                    if(pokedex[n_pkmn_guest].get_gen() == pokedex[n_pkmn_mystere].get_gen()):
                        indice_gen = "True"
                    else:
                        if(pokedex[n_pkmn_guest].get_gen() <= pokedex[n_pkmn_mystere].get_gen()):
                            indice_gen = "More"
                        else:
                            indice_gen = "Less"

                    feedback = {}
                    feedback["id"] = indice_id
                    feedback["name"] = indice_name
                    feedback["type1"] = indice_type1
                    feedback["type2"] = indice_type2
                    feedback["height"] = indice_height
                    feedback["weight"] = indice_weight
                    feedback["gen"] = indice_gen

                    print("ID               : " + str(pokedex[n_pkmn_guest].get_id()) + " - " + indice_id)
                    print("Name             : " + str(pokedex[n_pkmn_guest].get_name()) + " - " + str(indice_name))
                    print("Type 1           : " + str(pokedex[n_pkmn_guest].get_type1()) + " - " + indice_type1)
                    print("Type 2           : " + str(pokedex[n_pkmn_guest].get_type2()) + " - " + indice_type2)
                    print("Height Meters    : " + str(pokedex[n_pkmn_guest].get_height()) + " - " + indice_height)
                    print("Weight Kilograms : " + str(pokedex[n_pkmn_guest].get_weight()) + " - " + indice_weight)
                    print("Generation       : " + str(pokedex[n_pkmn_guest].get_gen()) + " - " + indice_gen)
                    print("\n")

                    play += 1

                else:
                    print("ID of Pokemon start at 1 !\n")
            else:
                print("It's not an ID of Pokemon !\n")