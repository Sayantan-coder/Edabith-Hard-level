def make_big_smaller_number(num_list: list) -> list:
    length = 0
    new_weighted_list = []
    for _ in num_list:
        length += 1
    if length == 0:
        return new_weighted_list
    small_num = num_list[0]
    for current in num_list:
        if current < small_num:
            small_num = current
    remove_amount = 0
    for num in num_list:
        if num != small_num:
            remove_portion = num * 0.25
            remove_amount = remove_amount + remove_portion
    for num in num_list:
        if num == small_num:
            value = num + remove_amount
            new_weighted_list += [value]
        else:
            value = num - (num * 0.25)
            new_weighted_list += [value]
    return new_weighted_list


print(make_big_smaller_number([2, 4, 8, 34, 23]))
print(make_big_smaller_number([16, 10, 8]))
print(make_big_smaller_number([21, 12, 43, 5, 54]))
