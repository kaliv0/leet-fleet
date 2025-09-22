# 167. Two Sum II - Input Array Is Sorted
from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        num_sum = numbers[left] + numbers[right]
        if num_sum == target:
            return [left + 1, right + 1]
        if num_sum > target:
            right -= 1
        if num_sum < target:
            left += 1


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]
