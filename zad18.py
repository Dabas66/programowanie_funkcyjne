def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

matrix = [
    [3, 6, 9],
    [9, 5, 7],
    [1, 1, 3]
]
transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)
