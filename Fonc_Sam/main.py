from matchup import compare
from team_building import random_team, team_weakness_counts
from data_loader import load_dataframe, get_pokemon
from analyse_pokemon import weaknesses, resistance, immunities
from type_chart import multiplier
import random


def random_matchup():
    df = load_dataframe("database/pokemon_data.csv")
    names = df["Name"].tolist()
    name1, name2 = random.sample(names, 2)

    p1 = get_pokemon(df, name1)
    p2 = get_pokemon(df, name2)

    verdict, explanation = compare(p1, p2)

    print("\n=== RANDOM MATCHUP ===")
    print(f"{p1.name} ({p1.type1}/{p1.type2}) VS {p2.name} ({p2.type1}/{p2.type2})")
    print(verdict)
    print(explanation)
    
def team_vs_team(team_a, size=6, weak_limit=2):
    df = load_dataframe("database/pokemon_data.csv")

    # Générer Team B UNE SEULE FOIS, différente de A
    excluded = {p.name.lower() for p in team_a}

    team_b = []
    while len(team_b) < size:
        candidate = random_team(size=1, weak_limit=weak_limit)[0]
        if candidate.name.lower() not in excluded:
            team_b.append(candidate)
            excluded.add(candidate.name.lower())

    score_a = score_b = 0

    print("\n=== TEAM VS TEAM ===")
    for i in range(size):
        a = team_a[i]
        b = team_b[i]

        verdict, _ = compare(a, b)
        print(f"Match {i+1}: {a.name} vs {b.name} -> {verdict}")

        if a.name in verdict:
            score_a += 1
        elif b.name in verdict:
            score_b += 1

    print("\n=== RESULTAT FINAL ===")
    if score_a > score_b:
        print("🏆 TEAM A gagne")
    elif score_b > score_a:
        print("🏆 TEAM B gagne")
    else:
        print("⚖️ Egalité")


def main():
    

    random_matchup()

    print("\n=== RANDOM TEAM ===")
    team = random_team(size=6, weak_limit=2)

    for p in team:
        print("-", p.name, p.type1, p.type2)

    print("\nWeakness counts:", team_weakness_counts(team))

    # ✅ Team vs Team : on utilise la MÊME team A affichée
    team_vs_team(team)





if __name__ == "__main__":
    main()
