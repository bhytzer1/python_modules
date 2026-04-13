def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    cap_seed = seed_type.capitalize()
    form_unit = unit.lower()

    if form_unit == "packets":
        print(f"{cap_seed} seeds: {quantity} packets available")
    elif form_unit == "grams":
        print(f"{cap_seed} seeds: {quantity} grams available")
    elif form_unit == "area":
        print(f"{cap_seed} seeds: covers {quantity} square available")
    else:
        print("Unknown unit type")
