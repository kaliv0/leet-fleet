# 78. Subsets
def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    dfs(nums, candidate=[], res=res)
    return res


def dfs(nums: list[int], candidate: list[int], res: list[list[int]]) -> None:
    res.append(candidate)

    for i in range(len(nums)):
        next_candidate = candidate + [nums[i]]
        next_nums = nums[i + 1:]
        dfs(next_nums, next_candidate, res)


if __name__ == "__main__":
    for nums, res in (
            ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
            ([0], [[], [0]])
    ):
        actual = subsets(nums)
        actual.sort()
        res.sort()
        assert actual == res, actual
