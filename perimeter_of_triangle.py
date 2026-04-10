def calculate_perimeter(points_list: list) -> float:
    side1 = (points_list[1][0] - points_list[0][0]) ** 2 + (
        points_list[1][1] - points_list[0][1]
    ) ** 2
    side2 = (points_list[2][0] - points_list[1][0]) ** 2 + (
        points_list[2][1] - points_list[1][1]
    ) ** 2
    side3 = (points_list[0][0] - points_list[2][0]) ** 2 + (
        points_list[0][1] - points_list[2][1]
    ) ** 2
    total_perimeter = (side1) ** 0.5 + (side2) ** 0.5 + (side3) ** 0.5
    return round(total_perimeter, 2)


print(calculate_perimeter([[15, 7], [5, 22], [11, 1]]))
print(calculate_perimeter([[0, 0], [0, 1], [1, 0]]))
print(calculate_perimeter([[-10, -10], [10, 10], [-10, 10]]))
