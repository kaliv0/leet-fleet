# 47. Permutations II
def permute_unique(nums: list[int]) -> list[list[int]]:
    nums.sort()
    
    res = []
    dfs(nums, [], res)
    return res


def dfs(nums, candidate, res):
    if len(nums) == 0:
        res.append(candidate)

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        new_candidate = candidate + [nums[i]]
        sub_nums = nums[:i] + nums[i + 1:]
        dfs(sub_nums, new_candidate, res)


if __name__ == '__main__':
    for nums, res in (
            ([1, 1, 2],
             [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
            ([1, 2, 3],
             [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            ([3, 3, 0, 3],
             [[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]])
    ):
        assert (actual := permute_unique(nums)) == res, actual
