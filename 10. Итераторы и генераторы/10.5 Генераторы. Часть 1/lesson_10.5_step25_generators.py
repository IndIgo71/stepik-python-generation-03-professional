def matrix_by_elem(matrix):
    yield from (elem for row in matrix for elem in row)
