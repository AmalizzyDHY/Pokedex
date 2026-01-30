from typing import Tuple
from pokemon import Pokemon
from type_chart import multiplier
from analyse_pokemon import weaknesses, resistance, immunities




def _attacker_types(attacker: Pokemon):
    """Retourne la liste des types de l'attaquant (1 ou 2)."""
    types = [attacker.type1]
    if attacker.type2 is not None:
        types.append(attacker.type2)
    return types

def best_offense(attacker: Pokemon, defender: Pokemon) -> Tuple[float, str]:
    """
    Meilleur multiplicateur possible de attacker sur defender.
    Retour: (best_mult, best_type)
    """
    best_mult = -1.0
    best_type = attacker.type1

    for t in _attacker_types(attacker):
        m = multiplier(t, defender)
        if m > best_mult:
            best_mult = m
            best_type = t

    return best_mult, best_type

def worst_threat(defender: Pokemon, attacker: Pokemon) -> Tuple[float, str]:
    """
    Plus grosse menace (le multiplicateur le plus élevé) que attacker peut infliger à defender.
    Retour: (worst_mult, threat_type)
    """
    worst_mult = -1.0
    threat_type = attacker.type1

    for t in _attacker_types(attacker):
        m = multiplier(t, defender)
        if m > worst_mult:
            worst_mult = m
            threat_type = t

    return worst_mult, threat_type

def matchup_score(attacker: Pokemon, defender: Pokemon) -> Tuple[float, str]:
    """
    Score simple de attacker contre defender + explication courte.
    Utilise:
      - best_offense(attacker, defender)
      - worst_threat(attacker, defender) -> menace que defender pose à attacker
    """
    off_mult, off_type = best_offense(attacker, defender)
    threat_mult, threat_type = worst_threat(attacker, defender)  # menace du defender sur attacker

    # Base = puissance offensive
    score = off_mult

    # Bonus/malus défense (comment attacker encaisse le defender)
    # (Tu peux ajuster ces valeurs si tu veux)
    if threat_mult == 0.0:
        score += 2.0      # immunité
    elif threat_mult == 0.5:
        score += 0.5      # bonne résistance
    elif threat_mult == 2.0:
        score -= 0.8      # faiblesse
    elif threat_mult == 4.0:
        score -= 1.6      # très grosse faiblesse

    exp = (f"Offense best: {attacker.name} uses {off_type} -> x{off_mult} | "
           f"Threat: {defender.name} can hit {attacker.name} with {threat_type} -> x{threat_mult}")
    return score, exp

def compare(a: Pokemon, b: Pokemon, margin: float = 0.2) -> Tuple[str, str]:
    """
    Compare deux Pokémon et renvoie (verdict, explication).
    margin sert à éviter de déclarer un avantage pour une différence minuscule.
    """
    score_a, exp_a = matchup_score(a, b)
    score_b, exp_b = matchup_score(b, a)

    explanation = (
        f"{a.name} ({a.type1}/{a.type2}) vs {b.name} ({b.type1}/{b.type2})\n"
        f"Score {a.name}: {score_a:.2f}\n"
        f"Score {b.name}: {score_b:.2f}\n"
        f"- {exp_a}\n"
        f"- {exp_b}\n"
    )

    if score_a > score_b + margin:
        verdict = f"✅ Avantage: {a.name}"
    elif score_b > score_a + margin:
        verdict = f"✅ Avantage: {b.name}"
    else:
        verdict = "⚖️ Match équilibré"

    return verdict, explanation

