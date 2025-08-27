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
    assert (actual := pivot_array(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10)) == [9, 5, 3, 10, 10, 12, 14], actual
    assert (actual := pivot_array(nums=[-3, 4, 3, 2], pivot=2)) == [-3, 2, 4, 3], actual
