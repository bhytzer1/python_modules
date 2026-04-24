#!/usr/bin/env python3
class GardenError(Exception):
    def __init__(self, message=""):
        super().__init__(message)

class PlantError(GardenError):
    def __init__(self, message="The tomato plant is wilting!"):
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)

def test_custom_errors() -> None:
    print("\nTesting PlantError...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        raise PlantError()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nAll custom error types work correctly!")

if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    test_custom_errors()
