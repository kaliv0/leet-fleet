# 2915. Length of the Longest Subsequence That Sums to Target
def length_of_longest_subsequence(nums: list[int], target: int) -> int:
    dp = [-1] * (target + 1)
    dp[0] = 0

    for num in nums:
        for val in range(target, num - 1, -1):
            if dp[val - num] != -1:
                dp[val] = max(dp[val - num] + 1, dp[val])

    return dp[target]


if __name__ == "__main__":
    for nums, target, res in (
            ([1, 2, 3, 4, 5], 9, 3),  # [1,3,5], and [2,3,4]
            ([4, 1, 3, 2, 1, 5], 7, 4),  # [1,3,2,1]
            ([1, 1, 5, 4, 5], 3, -1),
    ):
        assert (actual := length_of_longest_subsequence(nums, target)) == res, f"{actual} != {res}"
