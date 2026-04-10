def power_ranger(power: int, minimum: int, maximum: int):
    starting_base = minimum ** (1 / power)
    if int(starting_base) ** power < minimum:
        start_base = int(starting_base) + 1
    else:
        start_base = int(starting_base)
    ending_base = maximum ** (1 / power)
    if int(ending_base) ** power > maximum:
        end_base = int(ending_base)
    else:
        end_base = int(ending_base)
    count = (end_base - start_base) + 1
    return count


print(power_ranger(2, 49, 65))
print(power_ranger(3, 1, 27))
print(power_ranger(5, 31, 33))
print(power_ranger(4, 250, 1300))
