#!/usr/bin/env python3
import sys
import math

def get_player_pos() -> tuple:
    while True:
        text = input("Enter new coordinate as floats in format 'x,y,z': ")
        parts = text.split(',')
        if len(parts) != 3:
            print("Invalid syntax")
        else:
            try:
                x = float(parts[0])
                y = float(parts[1])
                z = float(parts[2])
                return(x, y, z)
            except ValueError:
                print("Conversion error")

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    cor1 = get_player_pos()
    print(f"Got a first tuple: {cor1}")
    print(f"It includes: X={cor1[0]}, Y={cor1[1]}, Z={cor1[2]}")
    distance = math.sqrt(cor1[0]**2 + cor1[1]**2 + cor1[2]**2)
    print(f"Distance to center: {distance:.4f}")
    print("Get a second set of coordinates")
    cor2 = get_player_pos()

    Ax = cor1[0] - cor2[0]
    Ay = cor1[1] - cor2[1]
    Az = cor1[2] - cor2[2]

    distance_total = math.sqrt(Ax**2 + Ay**2 + Az**2)
    print(f"Distance between the 2 sets of coordinates: {distance_total:.4f}")
