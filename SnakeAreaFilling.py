def get_numbers_of_time_eat(n: int) -> int:
    screen_size = n * n
    numbers_snake_eat = 0
    for x in range(n, 0, -1):
        if 2**x <= screen_size:
            numbers_snake_eat = x
            break
    return numbers_snake_eat


print(get_numbers_of_time_eat(8))
print(get_numbers_of_time_eat(7))
print(get_numbers_of_time_eat(6))
print(get_numbers_of_time_eat(24))
