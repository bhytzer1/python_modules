#!/usr/bin/env python3
import random

def gen_player_achievements() -> set:
    achievements = [
        "sgargabonzato",
        "sbrodolato",
        "fattocacca",
        "nooob",
        "pro",
        "hacker",
    ]
    numero_trofei = random.randint(1, 5)
    gabriele = random.sample(achievements, numero_trofei)
    return(set(gabriele))

if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    jacopetta = gen_player_achievements()
    paolo = gen_player_achievements()
    enrico = gen_player_achievements()
    iristide = gen_player_achievements()

    print((f"Player jacopetta: {jacopetta}"))
    print((f"Player paolo: {paolo}"))
    print((f"Player enrico: {enrico}"))
    print((f"Player iristide: {iristide}\n"))

    all_achievements = set().union(jacopetta, paolo, enrico, iristide)
    print(f"All distinct achievements: {all_achievements}")
    print("---------------------------------")

    common_achievemnts = jacopetta.intersection(paolo, enrico, iristide)
    print(f"Common achievements: {common_achievemnts}")
    print("---------------------------------")

    O_jacopetta = jacopetta.difference(paolo, enrico, iristide)
    O_paolo = paolo.difference(jacopetta, enrico, iristide)
    O_enrico = enrico.difference(jacopetta, paolo, iristide)
    O_iristide = iristide.difference(jacopetta, paolo, enrico)

    print(f"Only jacopetta has: {O_jacopetta}")
    print(f"Only enrico has: {O_enrico}")
    print(f"Only paolo has: {O_paolo}")
    print(f"Only iristide has: {O_iristide}")
    print("---------------------------------")

    missing_jacopetta = all_achievements.difference(jacopetta)
    missing_paolo = all_achievements.difference(paolo)
    missing_enrico = all_achievements.difference(enrico)
    missing_iristide = all_achievements.difference(iristide)

    print(f"jacopetta is missing: {missing_jacopetta}")
    print(f"enrico is missing: {missing_enrico}")
    print(f"paolo is missing: {missing_paolo}")
    print(f"iristide is missing: {missing_iristide}\n")
