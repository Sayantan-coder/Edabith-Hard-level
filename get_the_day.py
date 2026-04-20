import datetime


def get_day(date: str) -> str:
    Date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    day_value = Date.weekday()
    days = {
        6: "Sunday",
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thrusday",
        4: "Friday",
        5: "Saturday",
    }
    day_name = days[day_value]
    return day_name


print(get_day("12/07/2016"))
print(get_day("09/04/2016"))
print(get_day("07/11/2002"))
