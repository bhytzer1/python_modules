#!/usr/bin/env python3
def input_temperature(temp_str: str) -> int:
    return int(temp_str)

def test_temperature() -> None:
    print(f"{input_temperature('25')}")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"{e}")
    print("\n=== All tests completed, program didn't crash! ===")

if __name__ == "__main__"
    print("=== Garden Temperature ===\n")
    print(f"Input data is '{input_temperature('25')'}")

