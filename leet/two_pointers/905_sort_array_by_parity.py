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
    assert sort_array_by_parity([3, 1, 2, 4]) in ([2, 4, 3, 1], [4, 2, 3, 1], [4, 2, 1, 3], [2, 4, 1, 3])
    assert sort_array_by_parity([]) == []
    assert sort_array_by_parity([1]) == [1]
    assert sort_array_by_parity([1, 2]) == [2, 1]
