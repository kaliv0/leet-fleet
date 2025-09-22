# 45. Jump Game II


from typing import List


def jump(nums: List[int]) -> int:
    jumps = 0
    reachable = 0
    position = 0
    for i in range(len(nums) - 1):
        reachable = max(reachable, i + nums[i])
        if i == position:
            position = reachable
            jumps += 1
    return jumps


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    # output -> 2

    # nums = [2,3,0,1,4]
    # output -> 2

    # nums = [2, 3, 1]
    # output -> 1

    # nums = [1, 1, 3, 1, 1]
    # output -> 3

    print(jump(nums))
