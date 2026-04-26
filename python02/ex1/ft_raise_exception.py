#!/usr/bin/env python3


def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    else:
        return temp


def test_temperature() -> None:
    print(f"input data is '{input_temperature('25')}'")
    print(f"Temperature is now {input_temperature('25')}°C\n")
    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print("\nAll tests completed - program didn't crash!")


def temperature_control(sensore: int) -> None:
    if sensore > 40:
        return print(f"{sensore}°C is too hot for plants (max 40°C)")
    elif sensore < 0:
        return print(f"{sensore}°C is too cold for plants (min 0°C)")
