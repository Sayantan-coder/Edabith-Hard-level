def is_disarium_number(num: int) -> bool:
    def sum_digit_position(num_str: str, pos: int = 0):
        if len(num_str) == 0:
            return 0
        else:
            current_sum = int(num_str[0]) ** (pos + 1)
            return current_sum + sum_digit_position(num_str[1:], pos + 1)

    total_sum_value = sum_digit_position(str(num))
    if total_sum_value == num:
        return True
    else:
        return False


print(is_disarium_number(75))
print(is_disarium_number(135))
print(is_disarium_number(544))
print(is_disarium_number(518))
print(is_disarium_number(466))
print(is_disarium_number(8))
