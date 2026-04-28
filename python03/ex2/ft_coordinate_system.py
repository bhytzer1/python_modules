#!/usr/bin/env python3
import sys

def get_player_pos():
    while True:
        text = input("Enter new coordinate as floats in format 'x,y,z': ")
        parts = text.split(',')
        if len(parts) != 3:
            print("Invalid syntax")
        else:
            try:
                for parts in range(2):
                    if parts == 0:
                        x = float(0)
                    elif parts == 1:
                        y = float(1)
                    elif parts == 2:
                        z = float(2)
                    else:
                        return print("errore in 'conversione'")
            except:

