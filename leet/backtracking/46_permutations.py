# 46. Permutations
def permute(nums: list[int]) -> list[list[int]]:
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums: list[int], candidate: list[int], res: list[list[int]]):
    if len(nums) == 0:
        # we've traversed all nums
        res.append(candidate)
        return

    for i in range(len(nums)):
        new_candidate = candidate + [nums[i]]
        # NB: we pass all other nums except current one e.g. nums[i]
        sub_nums = nums[:i] + nums[i + 1:]
        dfs(sub_nums, new_candidate, res)


if __name__ == '__main__':
    for nums, res in (
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            ([0, 1], [[0, 1], [1, 0]]),
            ([1], [[1]]),
    ):
        assert (actual := permute(nums)) == res, actual
