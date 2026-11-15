# 905. Sort Array By Parity
def sort_array_by_parity(nums: list[int]) -> list[int]:
    res = []
    even = odd = -1
    # find all even nums
    while even < len(nums) - 1:
        even += 1
        if nums[even] % 2 == 0:
            res.append(nums[even])

    # find all odd nums
    while odd < len(nums) - 1:
        odd += 1
        if nums[odd] % 2 != 0:
            res.append(nums[odd])

    return res


if __name__ == "__main__":
    cases = [
        ([3, 1, 2, 4], ([2, 4, 3, 1], [4, 2, 3, 1], [4, 2, 1, 3], [2, 4, 1, 3])),
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
    ]

    for nums, result in cases:
        actual = sort_array_by_parity(nums)
        if isinstance(result, tuple):
            assert actual in result, actual
        else:
            assert actual == result, actual
