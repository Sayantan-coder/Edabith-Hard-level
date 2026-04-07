def is_disarium_number(num: int) -> bool:
    num_str = str(num)
    value = 0
    for ind in range(len(num_str)):
        value = value + int(num_str[ind]) ** (ind + 1)
    number = int(num_str)
    if value == number:
        return True
    else:
        return False


print(is_disarium_number(75))
print(is_disarium_number(135))
print(is_disarium_number(544))
print(is_disarium_number(518))
print(is_disarium_number(466))
print(is_disarium_number(8))
