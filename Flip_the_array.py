def flip_array(array_list: list) -> list:
    flip_list = []

    if len(array_list) == 0:
        return flip_list
    if type(array_list[0]) == list:
        for ind in range(len(array_list)):
            flip_list = flip_list + [array_list[ind][0]]
    else:
        for ind_ in range(len(array_list)):
            flip_list = flip_list + [[array_list[ind_]]]
    return flip_list


print(flip_array([1, 2, 3, 4]))
print(flip_array([[5], [6], [9]]))
print(flip_array([]))
