def ft_count_harvest_iterative() -> None:
    days_total = int(input("Days until harvest: "))
    for day in range(1, days_total + 1):
        print(f"Day {day}")
    print("Harvest time!")
