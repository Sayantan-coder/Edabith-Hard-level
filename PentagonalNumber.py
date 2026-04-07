def number_of_dots(value: int) -> int:
    if value == 1:
        return 1
    else:
        number_dots = number_of_dots(value - 1) + 5 * (value - 1)
        return number_dots


print(number_of_dots(3))
print(number_of_dots(6))
print(number_of_dots(4))
print(number_of_dots(9))
