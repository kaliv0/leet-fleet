# 56. Merge Intervals
def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort()

    res = []
    start, end = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] > end:
            res.append([start, end])
            start, end = curr
        else:
            # current interval might be nested within the previous one (e.g. [1, 4], [2, 3])
            end = max(end, curr[1])

    # NB: append final one
    res.append([start, end])
    return res


if __name__ == "__main__":
    for intervals, result in (
            ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
            ([[1, 4], [2, 3]], [[1, 4]]),
            ([[1, 4], [4, 5]], [[1, 5]]),
            ([[4, 7], [1, 4]], [[1, 7]]),
    ):
        assert (actual := merge(intervals)) == result, actual
