#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print(f"input data is '{input_temperature('25')}'")
    print(f"Temperature is now {input_temperature('25')}°C\n")
    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")

if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()

