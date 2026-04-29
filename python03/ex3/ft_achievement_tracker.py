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
    FilippoBonsignoreOttavoDiSavoia = gen_player_achievements()

    print((f"Player jacopetta: {jacopetta}"))
    print((f"Player paolo: {paolo}"))
    print((f"Player enrico: {enrico}"))
    print((f"Player FilippoBonsignoreOttavoDiSavoia: {FilippoBonsignoreOttavoDiSavoia}\n"))

    all_achievements = set().union(jacopetta, paolo, enrico, FilippoBonsignoreOttavoDiSavoia)
    print(f"All distinct achievements: {all_achievements}")
    print("---------------------------------")

    common_achievemnts = jacopetta.intersection(paolo, enrico, FilippoBonsignoreOttavoDiSavoia)
    print(f"Common achievements: {common_achievemnts}")
    print("---------------------------------")

    O_jacopetta = jacopetta.difference(paolo, enrico, FilippoBonsignoreOttavoDiSavoia)
    O_paolo = paolo.difference(jacopetta, enrico, FilippoBonsignoreOttavoDiSavoia)
    O_enrico = enrico.difference(jacopetta, paolo, FilippoBonsignoreOttavoDiSavoia)
    O_filippoBonsignoreOttavoDiSavoia = FilippoBonsignoreOttavoDiSavoia.difference(jacopetta, paolo, enrico)

    print(f"Only jacpoetta has: {O_jacopetta}")
    print(f"Only enrico has: {O_enrico}")
    print(f"Only paolo has: {O_paolo}")
    print(f"Only filippoBonsignoreOttavoDiSavoia has: {O_filippoBonsignoreOttavoDiSavoia}\n")
