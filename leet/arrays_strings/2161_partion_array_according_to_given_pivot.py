# 2161. Partition Array According to Given Pivot
def pivot_array(nums: list[int], pivot: int) -> list[int]:
    smaller = []
    bigger = []
    pivots = []
    for n in nums:
        if n < pivot:
            smaller.append(n)
        elif n == pivot:
            pivots.append(n)
        else:
            bigger.append(n)
    return smaller + pivots + bigger


if __name__ == "__main__":
    for nums, pivot, result in (
        ([9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14]),
        ([-3, 4, 3, 2], 2, [-3, 2, 4, 3]),
    ):
        assert (actual := pivot_array(nums, pivot)) == result, actual
