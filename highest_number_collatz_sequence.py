def max_collatz(n):
    current = n
    maximum = n

    while current != 1:

        if current % 2 == 0:
            current = current / 2
        else:

            current = current * 3 + 1

        if current > maximum:
            maximum = current

    return int(maximum)


print(max_collatz(10))
print(max_collatz(32))
print(max_collatz(85))
