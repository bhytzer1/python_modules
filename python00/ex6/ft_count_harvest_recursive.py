def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))
    helper_recursive(1, days)

def helper_recursive(actual_day: int, final_day: int):
    if (actual_day >= final_day + 1):
        print("Harvest time!")
        return
    else:
        print(f"Day {actual_day}")
        helper_recursive(actual_day + 1, final_day)
