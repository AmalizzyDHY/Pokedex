# Pokedex

## Project summary
As part of our studies, we had a course on advanced Python for AI. This led us to work in a group of three on a project called ‘Intelligent Pokédex’. We had to implement several features that we had imagined and coded ourselves.

UML :
|
| poulpe.py
| README.md
| pokemon_data.csv
|
|- - - Fonc_Sam
|       |- - - pycache
|       |- - - database
|       | _init_.py
|       | analyse_pokemon.py
|       | data_loader.py
|       | main.py
|       | matchup.py
|       | pokemon.py
|       | team_building.py
|       | type_chart.py
|       | info.txt
|
|- - - Fonc_Lisa
|       |- - - pycache
|       | _init_.py
|       | ai.py
|       | donnee_supp.py
|       | main.py
|       | pokedle.py
|       | pokemon.py
|       | traitement_db.py
|       | info.txt
|
|- - - Fonc_Gwen
|       |- - - poke_pics
|       | class_to_idx.json
|       | clustering.py
|       | cnn_predict_test.py
|       | cnn_train_extract.py
|       | cnn_train.py
|       | main.py
|       | pokemon_clusters_tsne.html
|       | pokemon_cnn.pt
|       | pokemon_features.npy
|       | pokemon_labels.npy
|       | predict_test.py
|       | template_matching.py
|       | test.png
|       | test1.png
|       | info.txt

Here are the features implemented by each of us:

Samuel:
- A Pokémon team generator with as few weaknesses as possible.
- A Pokémon battle simulation (you can choose which Pokémon battle each other or not).
- A battle simulation between two teams of six Pokémon each.

Lisa:
- A Pokédex, a mix between Pokémon and Wordle.

Gwenolé:
- An AI that recognises Pokémon from an image
- An AI that creates clusters based on the appearance of Pokémon

## Installation tutorial
To install our project correctly.
First, you must have Python installed on your machine.

Then you need the following modules:
- panda
- csv

Next, you must git clone our project so that it is on your computer.
Finally, the main menu is located in poulpe.py. Just launch the programme to use Samuel and Lisa's features.
To use the features implemented by Gwenolé, go to Fonc_Gwen and run ‘predict_test.py’. More information is available in Fonc_Gwen/info.txt.

## For each feature implemented
For information on each feature, go to the Fonc_Sam, Fonc_Gwen and Fonc_Lisa folders, where you will find an info.txt file that explains everything.