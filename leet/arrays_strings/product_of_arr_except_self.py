# 238. Product of Array Except Self
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
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
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
