# 560. Subarray Sum Equals K
def subarray_sum(nums: list[int], k: int) -> int:
    # NB: working solution but exceeds speed limits for large inputs
    pref_sums = [0]
    for i in range(0, len(nums)):
        pref_sums.append(nums[i] + pref_sums[-1])

    count = 0
    # for every prefix state
    for i in range(1, len(pref_sums)):
        # check every subarr up to that point
        for j in range(1, i + 1):
            if pref_sums[i] - pref_sums[j - 1] == k:
                count += 1

    return count


def subarray_sum_opt(nums: list[int], k: int) -> int:
    curr_sum = 0
    count = 0
    pref_map = {0: 1}

    for n in nums:
        # compute prefix_sum on each step
        curr_sum += n
        # similarly to Pair Sum - check if corresponding prefix_sum state has already been encountered
        if (co_prev := curr_sum - k) in pref_map:
            # add its freq count to result
            # -> since nums can contain negative numbers, prefix_sum varies
            # -> we may encounter same val at different positions and freq_count will be > 1
            count += pref_map[co_prev]

        # add or increase frequency count of curr prefix_sum
        pref_map[curr_sum] = pref_map.get(curr_sum, 0) + 1

    return count


if __name__ == "__main__":
    cases = [
        # ([1, 1, 1], 2, 2),
        # ([1, 2, 3], 3, 2),
        ([1, -1, 0], 0, 3),
    ]

    for nums, k, res in cases:
        assert (actual := subarray_sum_opt(nums, k)) == res, \
            f"{actual} != {res} -> {nums=}, {k=}"
