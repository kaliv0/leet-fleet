# 189. Rotate Array

from typing import List


def rotate(nums: List[int], k: int) -> None:
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    # nums = [1, 2, 3, 4, 5, 6, 7]
    # k = 3
    # output -> [5,6,7,1,2,3,4]

    # nums = [-1, -100, 3, 99]
    # k = 2
    # output -> [3,99,-1,-100]

    nums = [1, 2]
    k = 3
    # output -> [2, 1]

    rotate(nums, k)
    print(nums)
