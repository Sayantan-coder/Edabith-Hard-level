def first_before_second(text: str, first: str, second: str) -> bool:
    first_last = -1
    second_first = len(text)
    for index in range(len(text)):
        if text[index] == first:
            first_last = index
        elif text[index] == second:
            if index < second_first:
                second_first = index
    if first_last < second_first:
        return True
    else:
        return False


print(first_before_second("knaves knew about waterfalls", "k", "w"))
print(first_before_second("happy birthday", "a", "y"))
print(first_before_second("precarious kangaroos", "k", "a"))
print(first_before_second("a rabbit jumps joyfully", "a", "j"))
