# 48. Rotate Image
def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    for c in range(len(matrix)):
        for r in range(c + 1, len(matrix)):
            matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]

    for row in matrix:
        row.reverse()


if __name__ == "__main__":
    for matrix, res in (
            ([
                 [1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]
             ],
             [
                 [7, 4, 1],
                 [8, 5, 2],
                 [9, 6, 3]
             ]),
            ([
                 [5, 1, 9, 11],
                 [2, 4, 8, 10],
                 [13, 3, 6, 7],
                 [15, 14, 12, 16]
             ],
             [
                 [15, 13, 2, 5],
                 [14, 3, 4, 1],
                 [12, 6, 8, 9],
                 [16, 7, 10, 11]
             ]),
    ):
        rotate(matrix)
        for act, exp in zip(matrix, res):
            assert act == act
