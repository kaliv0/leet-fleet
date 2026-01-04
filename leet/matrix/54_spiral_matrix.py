# 54. Spiral Matrix
def spiral_order(matrix: list[list[int]]) -> list[int]:
    res = []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # move right
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        top += 1

        # move down
        for r in range(top, bottom + 1):
            res.append(matrix[r][right])
        right -= 1

        # NB: the check seems odd at first -> we check if the current (bottom) row is still valid
        if top <= bottom:
            # move left
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:
            # move up
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1

    return res


if __name__ == "__main__":
    for matrix, res in (
            ([
                 [1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]
             ],
             [1, 2, 3, 6, 9, 8, 7, 4, 5]),
            #############################
            ([
                 [1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12]
             ],
             [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
            ),
    ):
        assert (actual := spiral_order(matrix)) == res, actual
