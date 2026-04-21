#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age_days = age

    def grow(self, amount: float) -> None:
        self.height += amount

    def age(self, days: int) -> None:
        self.age_days += days

    def __str__(self) -> str:
        return f"{self.name}: {self.height:.1f}cm, {self.age_days} days old"

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.age_days} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 30, 45)
    cactus = Plant("Cactus", 15, 120)

    rose.show()
    sunflower.show()
    cactus.show()
