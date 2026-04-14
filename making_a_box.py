def make_a_box(num: int) -> list:
    box_list = []
    for row in range(num):
        element = ""
        for column in range(num):
            if row == 0 or row == num - 1 or column == 0 or column == num - 1:
                element = element + "#"
            else:
                element += " "
        box_list.append(element)
    return box_list


print(make_a_box(4))
print(make_a_box(7))
print(make_a_box(5))
print(make_a_box(8))
