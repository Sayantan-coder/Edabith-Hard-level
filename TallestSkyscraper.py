def get_tallest_skyscraper(matrix: list) -> int:
    height_tallest_skyscraper = 0

    number_columns = len(matrix[0])
    for col in range(number_columns):
        count = 0
        for row in range(len(matrix)):
            if matrix[row][col] == 1:
                count += 1
            if count > height_tallest_skyscraper:
                height_tallest_skyscraper = count
    return height_tallest_skyscraper


print(get_tallest_skyscraper([[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]))
print(get_tallest_skyscraper([[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1]]))
print(get_tallest_skyscraper([[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]]))
