# 238. Product of Array Except Self


def product_except_self(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    prefix = 1
    suffix = 1

    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]

    for j in range(len(nums) - 1, -1, -1):
        result[j] *= suffix
        suffix *= nums[j]

    return result


if __name__ == "__main__":
    for nums, result in (
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ):
        assert (actual := product_except_self(nums)) == result, actual
