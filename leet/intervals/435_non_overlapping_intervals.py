# 435. Non-overlapping Intervals
def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    # since we are search fir overlapping intervals -> sort by interval ends
    intervals.sort(key=lambda x: x[1])

    res = 0
    _, end = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] < end:
            res += 1
        else:
            end = curr[1]

    return res


if __name__ == "__main__":
    for intervals, result in (
            ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
            ([[1, 2], [1, 2], [1, 2]], 2),
            ([[1, 2], [2, 3]], 0)
    ):
        assert (actual := erase_overlap_intervals(intervals)) == result, actual
