def rearranged_difference(num: int) -> int:
    digit_list = []
    temp_number = num
    if temp_number == 0:
        return 0
    else:
        while temp_number:
            digit = temp_number % 10
            digit_list.append(digit)
            temp_number //= 10
        length = 0
        for _ in digit_list:
            length += 1
        for i in range(length):
            for j in range(0, length - i - 1):
                if digit_list[j] > digit_list[j + 1]:
                    temp = digit_list[j]
                    digit_list[j] = digit_list[j + 1]
                    digit_list[j + 1] = temp

        max_number = 0
        for ind in range(length - 1, -1, -1):
            max_number = (max_number * 10) + digit_list[ind]
        min_number = 0
        for index in range(length):
            min_number = (min_number * 10) + digit_list[index]
        difference = max_number - min_number
        return difference


print(rearranged_difference(972882))
print(rearranged_difference(3320707))
print(rearranged_difference(90010))
