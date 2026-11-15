# 26. Remove Duplicates from Sorted Array


def remove_duplicates(nums: list[int]) -> int:
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


if __name__ == "__main__":
    for nums, k, expected in (
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ):
        assert (actual := remove_duplicates(nums)) == k, actual
        assert nums[:k] == expected, nums
