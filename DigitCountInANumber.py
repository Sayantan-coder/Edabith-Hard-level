def count_digit(number: int) -> int:
    if number == 0:
        return 1

    count = 0
    while number:
        last_digit = number % 10
        count += 1
        number = number // 10
    return count


print(count_digit(4466))
print(count_digit(544))
print(count_digit(121317))
print(count_digit(0))
print(count_digit(12345))
print(count_digit(1289396387328))


# Recursive way to solve the problem:-
def counts_digit(number: int) -> int:
    if -9 <= number <= 9:
        return 1
    else:
        return 1 + counts_digit(number // 10)


print(count_digit(4466))
print(count_digit(544))
print(count_digit(121317))
print(count_digit(0))
print(count_digit(12345))
print(count_digit(1289396387328))
