#!/usr/bin/env python3
from pathlib import Path
import sys

try:
    from ft_garden_data import Plant
except ModuleNotFoundError:
    sys.path.append(str(Path(__file__).resolve().parents[1] / "ex1"))
    from ft_garden_data import Plant


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    rose.show()
    starting_height = rose.height

    for temp in range(1, 7 + 1):
        print(f"=== Day {temp} ===")
        rose.age(1)
        rose.grow(0.8)
        rose.show()
    total = rose.height - starting_height
    print(f"Growth this week: {round(total, 1)}cm")
