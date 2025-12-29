# 57. Insert Interval
def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    # insert new_interval via binary search -> intervals are sorted
    _bin_search_insert(intervals, new_interval)

    # merge intervals
    res = []
    start, end = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] <= end:
            end = max(end, curr[1])
        else:
            res.append([start, end])
            start, end = curr

    res.append([start, end])
    return res


def _bin_search_insert(intervals: list[list[int]], new_interval: list[int]) -> None:
    left, right = 0, len(intervals)
    while left < right:
        mid = (left + right) // 2
        if intervals[mid][0] >= new_interval[0]:
            right = mid
        else:
            left = mid + 1

    intervals.insert(left, new_interval)


if __name__ == "__main__":
    for intervals, new_interval, result in (
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
    ):
        assert (actual := insert(intervals, new_interval)) == result, actual
