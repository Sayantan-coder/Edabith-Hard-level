def create_pichart(data: dict) -> dict:
    total_frequency = 0
    for data_item in data:
        total_frequency += data[data_item]
    pichart_list = {}
    for data_item in data:
        value = (data[data_item] / total_frequency) * 360
        pichart_list[data_item] = round(value, 1)
    return pichart_list


print(create_pichart({"a": 1, "b": 2}))
print(create_pichart({"a": 30, "b": 15, "c": 55}))
print(create_pichart({"a": 8, "b": 21, "c": 12, "d": 5, "e": 4}))
