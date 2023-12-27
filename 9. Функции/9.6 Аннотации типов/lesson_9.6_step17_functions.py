def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return {i + 1: matrix[i] for i in range(len(matrix))}
