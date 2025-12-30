# 90. Subsets II
def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    # sort nums and while backtracking skip dups
    nums.sort()

    res = []
    dfs(nums, candidate=[], res=res)
    return res


def dfs(nums: list[int], candidate: list[int], res: list[list[int]]) -> None:
    res.append(candidate)
    for i in range(len(nums)):
        # skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        new_candidate = candidate + [nums[i]]
        subnums = nums[i + 1:]
        dfs(subnums, new_candidate, res)


if __name__ == "__main__":
    for nums, res in (
            ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
            ([0], [[], [0]])
    ):
        actual = subsets_with_dup(nums)
        actual.sort()  # suboptimal workaround for comparison
        res.sort()
        assert actual == res, actual
