#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.set_height(height)
        self.set_age(age)

    def set_height(self, value: float) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value

    def get_height(self) -> float:
        return self._height

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("age update rejected")
        else:
            self._age = value

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
        pass


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25)
    print(f"\nHeight updated: {rose._height}")

    rose.set_age(30)
    print(f"Age updated: {rose._age}\n")

    rose.set_height(-5)
    rose.set_age(-10)

    print("\nCurrent state: ", end="")
    rose.show()
