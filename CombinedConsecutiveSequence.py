def is_consecutive_combo(list1: list, list2: list) -> bool:
    sort_list1 = sorted(list1)
    sort_list2 = sorted(list2)
    combo_list = sorted(sort_list1 + sort_list2)

    def get_max(combo_list):
        if len(combo_list) == 1:
            return combo_list[0]
        else:
            max = combo_list[0]
            rest_of_max = get_max(combo_list[1:])
            if max > rest_of_max:
                return max
            else:
                return rest_of_max

    def get_min(combo_list):
        if len(combo_list) == 1:
            return combo_list[0]
        else:
            min = combo_list[0]
            rest_of_min = get_min(combo_list[1:])
            if min < rest_of_min:
                return min
            else:
                return rest_of_min

    start = get_min(combo_list)
    end = get_max(combo_list)
    consecutive_list = [num for num in range(start, end + 1)]
    if combo_list == consecutive_list:
        return True
    else:
        return False


print(is_consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
print(is_consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
print(is_consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
print(is_consecutive_combo([44, 46], [45]))
