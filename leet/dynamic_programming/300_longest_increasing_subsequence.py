# 300. Longest Increasing Subsequence
def length_of_LIS(nums: list[int]) -> int:
    dp = [1] * len(nums)
    longest = 1  # keep track throughout instead of returning max(dp) at the end

    # loop from the begging up to every index in nums list
    for i in range(1, len(nums)):
        for j in range(i):
            # we sopt to consecutive increasing numbers
            if nums[i] > nums[j]:
                # update for current index (only if overall bigger value)
                dp[i] = max(dp[j] + 1, dp[i])
                longest = max(dp[i], longest)

    return longest


##############################
def patience_algo(nums: list[int]) -> int:
    tails = [0] * len(nums)
    size = 0

    for num in nums:
        i = _bin_search(num, tails, size)
        tails[i] = num
        size = max(i + 1, size)
    return size


def _bin_search(num, tails, size):
    l = 0
    r = size
    while l != r:
        mid = (l + r) // 2
        if tails[mid] < num:
            l = mid + 1
        else:
            r = mid
    return l


if __name__ == "__main__":
    for nums, res in (
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([0, 1, 0, 3, 2, 3], 4),
            ([7, 7, 7, 7, 7, 7, 7], 1),
    ):
        assert (actual := length_of_LIS(nums)) == res, f"{actual} != {res}"
