from matchup import compare
from team_building import random_team, team_weakness_counts
from data_loader import load_dataframe, get_pokemon
from analyse_pokemon import weaknesses, resistance, immunities
from type_chart import multiplier
import random


def random_matchup(df):
    names = df["Name"].tolist()
    name1, name2 = random.sample(names, 2)

    p1 = get_pokemon(df, name1)
    p2 = get_pokemon(df, name2)

    verdict, explanation = compare(p1, p2)

    print("\n=== RANDOM MATCHUP ===")
    print(f"{p1.name} ({p1.type1}/{p1.type2}) VS {p2.name} ({p2.type1}/{p2.type2})")
    print(verdict)
    print(explanation)


def main():
    # 1) Charger le dataset
    df = load_dataframe("database/pokemon_data.csv")

    # 2) Matchup aléatoire
    random_matchup(df)

    # 3) Générer une équipe aléatoire
    print("\n=== RANDOM TEAM ===")
    team = random_team(df, size=6, weak_limit=2)

    for p in team:
        print("-", p.name, p.type1, p.type2)

    print("\nWeakness counts:", team_weakness_counts(team))


if __name__ == "__main__":
    main()
