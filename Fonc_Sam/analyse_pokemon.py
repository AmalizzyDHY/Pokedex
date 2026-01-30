from type_chart import TYPES, multiplier
from pokemon import Pokemon



def weaknesses(defender: Pokemon) -> dict:
    """
    Retourne les types d'attaque qui font x2 ou plus au Pokémon.
    """
    w = {}
    for t in TYPES:
        m = multiplier(t, defender)
        if m >= 2.0:
            w[t] = m
    return w


def resistance(defender: Pokemon) -> dict:
    """
    Retourne les types d'attaque qui font x0.5 ou moins (mais pas 0).
    """
    r = {}
    for t in TYPES:
        m = multiplier(t, defender)
        if 0 < m <= 0.5:
            r[t] = m
    return r


def immunities(defender: Pokemon) -> list:
    """
    Retourne les types d'attaque auxquels le Pokémon est immunisé.
    """
    imm = []
    for t in TYPES:
        m = multiplier(t, defender)
        if m == 0.0:
            imm.append(t)
    return imm
