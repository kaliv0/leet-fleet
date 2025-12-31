# 198. House Robber

# top-down
def rob(nums: list[int]) -> int:
    memo = {}

    def _rob(nums, idx):
        # we passed beyond the last house (actually the first one as we are looping backwards)
        if idx < 0:
            return 0

        if idx not in memo:
            rob_curr = nums[idx] + _rob(nums, idx - 2)
            skip_curr = _rob(nums, idx - 1)
            memo[idx] = max(rob_curr, skip_curr)
        return memo[idx]

    return _rob(nums, idx=len(nums) - 1)


# bottom-up
def rob_alt(nums: list[int]) -> int:
    total = curr = 0
    for n in nums:
        # total shows what we have robbed in total so far
        # curr points to current decision to rob the house and increment total
        # or skip i.e. keep curr as it is
        total, curr = curr, max(curr, total + n)
    # we return curr and not total as it is already updated for the last house while total still lags behind
    return curr


if __name__ == "__main__":
    for nums, res in (
            ([1, 2, 3, 1], 4),
            ([2, 7, 9, 3, 1], 12)
    ):
        assert (actual := rob_alt(nums)) == res, actual
