# 228. Summary Ranges
def summary_ranges(nums):
    result = []
    start = 0
    for i in range(1, len(nums) + 1):
        prev = i - 1
        if i == len(nums) or nums[i] != nums[prev] + 1:
            if start == prev:
                result.append(str(nums[start]))
            else:
                result.append(f"{nums[start]}->{nums[prev]}")
            start = i
    return result


if __name__ == "__main__":
    for nums, ranges in (
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
    ):
        assert (actual := summary_ranges(nums)) == ranges, (
            f"{actual} != {ranges}, {nums=}"
        )
