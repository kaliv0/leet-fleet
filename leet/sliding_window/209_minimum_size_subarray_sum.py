# 209. Minimum Size Subarray Sum
def min_sub_array_len(target: int, nums: list[int]) -> int | float:
    min_len = float('inf')
    curr_sum = 0
    left = 0
    for right, num in enumerate(nums):
        curr_sum += num
        while curr_sum >= target:
            # move the left pointer to narrow the window and find the smallest length
            curr_sum -= nums[left]
            # update min_len to current length (right-left+1) if it's smaller
            min_len = min((right - left + 1), min_len)
            left += 1
    return 0 if min_len == float('inf') else min_len


if __name__ == '__main__':
    for target, nums, res in (
            (7, [2, 3, 1, 2, 4, 3], 2),
            (4, [1, 4, 4], 1),
            (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    ):
        assert (act := min_sub_array_len(target, nums)) == res, f'{act} != {res}'
