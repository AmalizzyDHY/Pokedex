from pokemon import Pokemon
import os
import csv

def traitementDB():
    # print("Dossier courant :", os.getcwd()) # Pour savoir où on est
    # print("Contenu du dossier :", os.listdir()) # Pour savoir ce qu'il y a avec nous
    # print("\n")
    
    # print("poulpe")
    pokedex = [] # array

    with open("pokemon_data.csv", newline='', encoding="utf-8") as fichier:
        test = csv.reader(fichier, delimiter=",")
        for ligne in test:
            #print(ligne)
            #print("\n")
            id = ligne[1]
            name = ligne[0]
            type1 = ligne[36]
            type2 = ligne[37]
            if ( type2 == ""):
                type2 = "Aucun"
            height = ligne[28]
            weight = ligne[30]
            gen = ligne[40]
            new_pokemon = Pokemon(id, name, height, weight, type1, type2, gen)
            pokedex.append(new_pokemon)
        
        # print(type(pokedex))
        # print("Template")
        # pokedex[0].show() # On affiche pour être sûr
        # print("\n")
        # print(pokedex[58])

    

    return pokedex