# 15. 3Sum
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    # sort to be able to apply variation of "two sum" algorithm
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        # if all nums are > 0 there is no way to get zero as a sum between any them
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1
        # nested "two sum" approach
        while j < k:
            local_sum = nums[i] + nums[j] + nums[k]
            if local_sum > 0:
                k -= 1
            if local_sum < 0:
                j += 1
            if local_sum == 0:
                if (local_res := [nums[i], nums[j], nums[k]]) not in result:
                    result.append(local_res)
                j += 1
                k -= 1
                # skip duplicates
                while j < len(nums) - 1 and nums[j] == nums[j - 1]:
                    j += 1
                while k > j and nums[k] == nums[k + 1]:
                    k -= 1

    return result


if __name__ == "__main__":
    assert three_sum([1, 0, -1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([-1, -1, -1, 0, 0, 1, 1, 1]) == [[-1, 0, 1]]
