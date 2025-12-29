# 452. Minimum Number of Arrows to Burst Balloons
def find_min_arrow_shots(points: list[list[int]]) -> int:
    # NB: sort by range end -> we are searching for overlapping intervals
    points.sort(key=lambda x: x[1])

    res = 1
    _, end = points[0]
    for i in range(1, len(points)):
        curr = points[i]
        if curr[0] > end:
            res += 1
            end = curr[1]

    return res


if __name__ == "__main__":
    for intervals, result in (
            ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
            ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
            ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
            ([[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]], 2),
            ([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]], 2)
    ):
        assert (actual := find_min_arrow_shots(intervals)) == result, actual
