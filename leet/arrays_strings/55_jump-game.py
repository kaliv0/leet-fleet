# 55. Jump Game


from typing import List


def can_jump(nums: List[int]) -> bool:
    reachable = 0
    for i, n in enumerate(nums):
        if i > reachable:
            return False
        reachable = max(reachable, (i + n))
    return True


if __name__ == '__main__':
    # nums = [2, 3, 1, 1, 4]
    # output -> True

    nums = [3, 2, 1, 0, 4]
    # output-> False

    print(can_jump(nums))
