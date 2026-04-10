def subtract_matrix(matrix1: list, matrix2: list):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        result = []
        for i in range(len(matrix1)):
            for j in range(len(matrix2)):
                if i == j:
                    value = [
                        matrix1[i][ind] - matrix2[j][ind]
                        for ind in range(len(matrix1[0]))
                    ]
                    result.append(value)
                    break

        return result
    else:
        return ValueError(
            "Dimension of two matrices must be same for subtract between two matrices"
        )


print(subtract_matrix([[9, 8, 7], [6, 5, 4]], [[7, 8, 9], [4, 5, 6], [1, 2, 3]]))
print(
    subtract_matrix(
        [[4, 5, 6], [6, 5, 4], [3, 2, 1]], [[1, 2, 3], [4, 5, 6], [3, 2, 1]]
    )
)
print(
    subtract_matrix(
        [[3, 2, 1], [6, 5, 4], [9, 8, 7]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    )
)
