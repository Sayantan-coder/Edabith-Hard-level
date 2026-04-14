def boolean_and(bool_list: list) -> bool:
    while len(bool_list) != 1:
        first = bool_list[0]
        second = bool_list[1]
        result = first and second
        bool_list = [result] + bool_list[2:]
    return bool_list[0]


def boolean_or(bool_list: list) -> bool:
    while len(bool_list) > 1:
        first = bool_list[0]
        second = bool_list[1]
        result = first or second
        bool_list = [result] + bool_list[2:]
    return bool_list[0]


print(boolean_and([False, False, True, False, True]))
print(boolean_and([True, True, True, False, False, True, False, False]))
print(boolean_or([False, False, True, False, True]))
print(boolean_or([True, True, True, False, False, True, False, False]))
