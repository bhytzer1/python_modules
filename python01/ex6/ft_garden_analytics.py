#!/usr/bin/env python3
from typing import cast


class Plant:
    class Stats:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self): self._grow_calls += 1
        def record_age(self): self._age_calls += 1
        def record_show(self): self._show_calls += 1

        def display(self):
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age_days = age
        self.stats = self.Stats()

    def grow(self, amount: float) -> None:
        self.height += amount
        self.stats.record_grow()

    def age(self, days: int) -> None:
        self.age_days += days
        self.stats.record_age()

    def __str__(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age_days} days old"

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")
        self.stats.record_show()

    @staticmethod
    def IsOlderThenAYear(days: int) -> bool:
        return days > 365

    @classmethod
    def CreateAnonymous(cls):
        return cls("Unknown plant", 0.0, 0)


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
    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_calls = 0

        def record_shade(self):
            self._shade_calls += 1

        def display(self):
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

        self.stats = self.TreeStats()

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height}cm long and {self.trunk_diameter}cm wide."
        )
        cast(Tree.TreeStats, self.stats).record_shade()

    def show(self) -> None:
        super().show()

        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int, harvest_season: str
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self, amount: float) -> None:
        super().grow(amount)

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_plant_statistic(plant: Plant) -> None:
    print(f"[statistic for {plant.name}]")
    plant.stats.display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.IsOlderThenAYear(30)}")
    print(f"Is 400 days more than a year? -> {Plant.IsOlderThenAYear(400)}")

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "Red")
    rose.show()
    display_plant_statistic(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.bloom()
    rose.show()
    display_plant_statistic(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistic(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistic(oak)

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "Yellow")
    sunflower.show()
    display_plant_statistic(sunflower)

    print("[make sunflower grow, age and bloom]")
    sunflower.grow(30.0)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_plant_statistic(sunflower)

    print("\n=== Anonymous")
    anon = Plant.CreateAnonymous()
    anon.show()
    display_plant_statistic(anon)
