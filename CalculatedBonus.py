def calculate_bonus(bill_day: int) -> int:
    total_bonus = 0
    if 0 <= bill_day <= 32:
        return total_bonus
    elif 33 <= bill_day <= 40:
        total_bonus += ((bill_day - 33) + 1) * 325
        return total_bonus
    elif 41 <= bill_day <= 48:
        total_bonus = total_bonus + (325 * 8) + ((bill_day - 41) + 1) * 550
        return total_bonus
    else:
        total_bonus = total_bonus + (8 * 325) + (550 * 8) + (bill_day - 48) * 600
        return total_bonus


print(calculate_bonus(33))
print(calculate_bonus(37))
print(calculate_bonus(41))
print(calculate_bonus(50))
