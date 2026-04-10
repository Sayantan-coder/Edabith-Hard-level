def factorial_of_factorial(number: int) -> int:
    result = 1
    for num in range(1, number + 1):
        factorial = 1

        for i in range(1, num + 1):
            factorial = factorial * i
        result = result * factorial
    return result


print(factorial_of_factorial(4))
print(factorial_of_factorial(5))
print(factorial_of_factorial(6))
