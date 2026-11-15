# 747. Largest Number At Least Twice of Others
def dominant_index(nums: list[int]) -> int:
    max_int = -1  # all nums are positive
    max_idx = -1
    for idx, n in enumerate(nums):
        if n > max_int:
            max_int = n
            max_idx = idx

    for idx, n in enumerate(nums):
        if idx != max_idx and n * 2 > max_int:
            return -1

    return max_idx


if __name__ == "__main__":
    for nums, result in (
        ([3, 6, 1, 0], 1),
        ([1, 2, 3, 4], -1),
        ([0, 0, 0, 1], 3),
    ):
        assert (actual := dominant_index(nums)) == result, actual
