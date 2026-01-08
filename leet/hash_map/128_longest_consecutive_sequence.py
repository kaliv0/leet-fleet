# 128. Longest Consecutive Sequence
def longestConsecutive(nums: list[int]) -> int:
    if len(nums) < 2:
        return len(nums)

    nums.sort()

    max_len = 1
    curr_len = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue
        if nums[i] == nums[i - 1] + 1:
            curr_len += 1
        else:
            max_len = max(curr_len, max_len)
            curr_len = 1

    max_len = max(curr_len, max_len)
    return max_len


def longestConsecutive_hash(nums: list[int]) -> int:
    num_set = set(nums)
    max_len = 0

    for num in num_set:
        if num - 1 not in num_set:
            # beginning of a new subsequence
            right_num = num + 1
            while right_num in num_set:
                # progress right to find end of sequence
                right_num += 1
            # NB: right_num - num returns length of sequence since by definition it's increasing by 1
            max_len = max(right_num - num, max_len)

    return max_len


if __name__ == '__main__':
    for nums, res in (
            ([100, 4, 200, 1, 3, 2], 4),
            ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
            ([1, 0, 1, 2], 3),
            ([], 0),
            ([1], 1),
            ([1, 2, 2, 3, 5, 6], 3)
    ):
        assert (act := longestConsecutive_hash(nums)) == res, f"{res} != {act}"
