def average_speed(up_time: int, up_rate: int, down_rate: int) -> int:
    up_distance_travel = (up_rate / 60) * up_time
    down_distance_travel = up_distance_travel
    total_distance_travel = up_distance_travel + down_distance_travel
    down_time = (60 / down_rate) * down_distance_travel
    total_time = up_time + down_time
    average_speed = (total_distance_travel / total_time) * 60
    return average_speed


print(average_speed(18, 20, 60))
print(average_speed(30, 10, 30))
print(average_speed(30, 8, 24))
