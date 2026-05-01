#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===\n")
    inventory = {}
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Invalid parameter: {arg}")
            continue
        parts = arg.split(':')
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
        else:
            key = parts[0]
            quantity = parts[1]
            try:
                quantity = int(parts[1])
                if quantity <= 0:
                    print(f"Error - quantity for '{key}' must be positive - discarding")
                if key in inventory:
                    print(f"Redundant item '{key}' - discarding")
                else:
                    inventory[key] = quantity
            except ValueError:
                print(f"Quantity error for '{key}': invalid literal for int() with base 10: '{quantity}'")
    print(f"Got inventory: {inventory}")
    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")
    num_obj = len(inventory)
    total_obj = sum(inventory.values())
    print(f"Total quantity of the {num_obj} items: {total_obj}")
    for item, qty in sorted(inventory.items()):
        if total_obj > 0:
            percentage = (qty / total_obj) * 100
            print(f"Item {item} represents {percentage:.1f}%")
    best_item = max(inventory, key=inventory.get)
    least_item = min(inventory, key=inventory.get)
    print(f"Item most abundant: {best_item} with quantity {max(inventory.values())}")
    print(f"Item least abundant: {least_item} with quantity {min(inventory.values())}")
    print("\n--- Event: Found a treasure chest! ---\n")
    print("you found 3 potion and 1 bow!")
    if 'potion' in inventory:
        inventory['potion'] += 3
    else:
        inventory['potion'] = 3

    if 'bow' in inventory:
        inventory['bow'] += 1
    else:
        inventory['bow'] = 1
    print(f"Updated inventory: {inventory}")
