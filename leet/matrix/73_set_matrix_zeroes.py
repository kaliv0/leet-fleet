# 73. Set Matrix Zeroes
def set_zeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    ...


if __name__ == "__main__":
    for matrix, res in (
            ([
                 [0, 1, 2, 0],
                 [3, 4, 5, 2],
                 [1, 3, 1, 5]
             ],
             [
                 [0, 0, 0, 0],
                 [0, 4, 5, 0],
                 [0, 3, 1, 0]
             ]),
            ##########################
            ([
                 [1, 1, 1],
                 [1, 0, 1],
                 [1, 1, 1]
             ],
             [
                 [1, 0, 1],
                 [0, 0, 0],
                 [1, 0, 1]
             ]),
    ):
        assert (actual := set_zeroes(matrix)) == res, actual
