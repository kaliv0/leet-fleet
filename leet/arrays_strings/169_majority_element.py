# 169. Majority Element

from collections import defaultdict
from typing import List


def majority_element(nums: List[int]) -> int:
    half_size = len(nums) // 2
    count_map = defaultdict(int)
    for n in nums:
        count_map[n] += 1
        if count_map[n] > half_size:
            return n


if __name__ == '__main__':
    nums = [3, 2, 3]
    # output -> 3

    nums = [2, 2, 1, 1, 1, 2, 2]
    # output -> 2

    print(majority_element(nums))
