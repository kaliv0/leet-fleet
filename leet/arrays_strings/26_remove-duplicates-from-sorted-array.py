# 26. Remove Duplicates from Sorted Array

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    cnt = 1
    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[j - 1]:
            nums[i] = nums[j]
            cnt += 1
            i += 1
    return cnt


if __name__ == '__main__':
    # nums = [1, 1, 2]
    # output -> 2, nums = [1,2,_]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # output -> 5, nums = [0,1,2,3,4,_,_,_,_,_]

    print(remove_duplicates(nums))
    print(nums)
