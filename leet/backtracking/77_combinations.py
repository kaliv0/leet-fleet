# 77. Combinations
def combine(n: int, k: int) -> list[list[int]]:
    res = []
    candidate = []
    dfs(range(1, n + 1), candidate, k, res)
    return res


def dfs(nums: range, candidate: list[int], k: int, res: list[list[int]]) -> None:
    # add candidate if meets criteria
    if len(candidate) == k:
        res.append(candidate)

    # progress for other combinations
    for i in range(len(nums)):
        new_candidate = candidate + [nums[i]]
        sub_nums = nums[i + 1:]
        dfs(sub_nums, new_candidate, k, res)


if __name__ == "__main__":
    for n, k, res in (
            (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
            (1, 1, [[1]])
    ):
        actual = combine(n, k)
        actual.sort()
        res.sort()
        assert actual == res, actual
