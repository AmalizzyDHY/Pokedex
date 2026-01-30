from collections import Counter
from pokemon import Pokemon
from analyse_pokemon import weaknesses, resistance, immunities
from data_loader import get_pokemon
from typing import List

import random


def team_weakness_counts(team):
    """
    Compte le nombre de Pokémon faibles à chaque type dans l'équipe.
    """
    counts = Counter()
    for p in team:
        for t in weaknesses(p).keys():
            counts[t] += 1
    return counts


def random_team(df, size=6, weak_limit=2):
    """
    Génère une équipe aléatoire en évitant les doublons de faiblesses.
    """
    import random

    names = df["Name"].tolist()
    team = []
    weakness_counts = Counter()

    while len(team) < size:
        name = random.choice(names)

        if any(p.name.lower() == name.lower() for p in team):
            continue

        candidate = get_pokemon(df, name)
        cand_weak = weaknesses(candidate)

        if any(weakness_counts[t] >= weak_limit for t in cand_weak):
            continue

        team.append(candidate)
        for t in cand_weak:
            weakness_counts[t] += 1

    return team
