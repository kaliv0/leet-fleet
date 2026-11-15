# 80. Remove Duplicates from Sorted Array II


def remove_duplicates(nums: list[int]) -> int:
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


if __name__ == "__main__":
    for nums, k, expected in (
        ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
        ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
    ):
        assert (actual := remove_duplicates(nums)) == k, actual
        assert nums[:k] == expected, nums
