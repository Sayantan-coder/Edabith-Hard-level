def find_fulcrum(num_list: list) -> int:
    length = 0
    for _ in num_list:
        length += 1
    if length < 3:
        return -1
    ind = 1
    while ind < length - 1:
        left_sum = 0
        i = 0
        while i < ind:
            left_sum = left_sum + num_list[i]
            i = i + 1
        right_sum = 0
        j = i + 1
        while j < length:
            right_sum = right_sum + num_list[j]
            j = j + 1
        if left_sum == right_sum:
            return num_list[ind]
        ind += 1
    return -1


print(find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]))
print(find_fulcrum([9, 1, 9]))
print(find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]))
print(find_fulcrum([8, 8, 8, 8]))
