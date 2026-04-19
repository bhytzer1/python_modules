#!/usr/bin/env python3
from pathlib import Path
import sys

try:
    from ft_garden_data import Plant
except ModuleNotFoundError:
    sys.path.append(str(Path(__file__).resolve().parents[1] / "ex1"))
    from ft_garden_data import Plant

if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    my_plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120)
    ]

    for p in my_plants:
        print("Created: ", end="")
        p.show()
