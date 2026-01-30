import pandas as pd

# 1. Charger la base
df = pd.read_csv('C:\Users\hp\OneDrive\Documents\Projet_python_avancé_M1\Pokedex\pokemon_data.csv')

# 2. Vérifier les types et les manquants
print("--- Vérification des colonnes ---")
print(df.info()) # Montre si les colonnes sont bien des nombres ou du texte

print("\n--- Vérification des Type 2 manquants ---")
print(df['Type 2'].isnull().sum()) # Compte combien n'ont pas de 2ème type