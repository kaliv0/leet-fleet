# 80. Remove Duplicates from Sorted Array II


from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) < 3:
        return len(nums)

    cnt = 2
    i = 2
    for j in range(2, len(nums)):
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            cnt += 1
            i += 1
    return cnt


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    # output -> 5, nums = [1,1,2,2,3,_]

    # nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    # output -> 7, nums = [0,0,1,1,2,3,3,_,_]

    print(remove_duplicates(nums))
    print(nums)
