#!/usr/bin/env python3
from pathlib import Path
import sys

try:
    from ft_garden_data import Plant
except ModuleNotFoundError:
    sys.path.append(str(Path(__file__).resolve().parents[1] / "ex1"))
    from ft_garden_data import Plant

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)

        self.color = color
        self.is_blooming = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        super().show()

        print(f"Color: {self.color}")
        if self.is_blooming:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float):
        super().__init__(name, height, age)

        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self.produce_shade = True

    def show(self) -> None:
        super().show()

        print(f"Trunk diameter: {self.trunk_diameter}")
        if self.produce_shade:
            return
        else:
            print(f"Tree {self.name} now produces a shade of {self.height}cm long and {self.trunk_diameter}cm wide.")


# class Vegetable(Plant):
#     def __init__(self, harvest_season: str):





if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()

    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show()
