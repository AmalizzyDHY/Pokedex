import pandas as pd
from pokemon import Pokemon


def load_dataframe(path: str) -> pd.DataFrame:
    """
    Charge et nettoie le dataset Pokémon.
    """
    df = pd.read_csv(path)

    # Nettoyage des colonnes
    df.columns = df.columns.str.strip()
    df['Name'] = df['Name'].astype(str).str.strip()
    df['Type 1'] = df['Type 1'].astype(str).str.strip()

    # Gestion du Type 2
    if 'Type 2' in df.columns:
        df['Type 2'] = df['Type 2'].fillna('None').astype(str).str.strip()
    else:
        raise ValueError("Colonne 'Type 2' absente du CSV.")

    return df



def get_pokemon(df, name: str) -> Pokemon:
    """
    Retourne un objet Pokemon à partir de son nom (insensible à la casse).
    """
    # Recherche insensible à la casse
    row = df[df['Name'].str.lower() == name.lower()]

    if row.empty:
        raise ValueError(f"Pokémon '{name}' not found in dataset.")

    row = row.iloc[0]

    type1 = row['Type 1']
    type2 = row['Type 2'] if row['Type 2'] != 'None' else None

    return Pokemon(
        name=row['Name'],
        type1=type1,
        type2=type2
    )
