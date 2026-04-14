def collatz(numa: int, numb: int) -> str:
    count_numa = 0
    count_numb = 0

    while numa != 1:
        is_even_numa = True if numa % 2 == 0 else False
        if is_even_numa:
            numa /= 2
            count_numa += 1
        else:
            numa = (numa * 3) + 1
            count_numa += 1
    while numb != 1:
        is_even_numb = True if numb % 2 == 0 else False
        if is_even_numb:
            numb /= 2
            count_numb += 1
        else:
            numb = (numb * 3) + 1
            count_numb += 1
    if count_numa > count_numb:
        return "b"
    else:
        return "a"


print(collatz(10, 15))
print(collatz(13, 16))
print(collatz(53782, 72534))
