#!/usr/bin/env python3
import sys
sys.path.append("../ex1")
from ft_garden_data import Plant

class plant(Plant):

    def grow(self) -> None:
        self.height += amount
    def age(self) -> None:
        self.age += days

def plant_growth(self) -> None:
    temp = 0
    rate = (self.height / self.age)



if __name__ == "__main__":
    print(f"=== Garden Plant Growth ===")
    rose = plant("Rose", 25.0, 30)
    rose.show()
    starting_height = rose.height

    for temp in range(1, 7 + 1):
        print(f"=== Day {temp} ===\n")
        print(f"{rose}")
        rose.age(1)
        rose.height(0.8)
        rose.show()
    total = rose.height - starting_height
    print(f"Growth this week: {round(total, 1)}cm")




