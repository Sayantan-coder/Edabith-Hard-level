import datetime


def has_friday_13(month: int, year: int) -> bool:
    date = datetime.date(year, month, 13)
    if date.weekday() == 4:
        return True
    else:
        return False


print(has_friday_13(3, 2020))
print(has_friday_13(10, 2017))
print(has_friday_13(1, 1985))
print(has_friday_13(4, 2026))
