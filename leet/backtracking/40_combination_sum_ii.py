# 40. Combination Sum II
def combination_sum_2(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()

    res = []
    dfs(candidates, target, [], res)
    return res


def dfs(nums, target, comb, res):
    # add to res if meets criteria
    if target == 0:
        res.append(comb[:])
        return
    if target < 0:
        return

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        curr_num = nums[i]
        comb.append(curr_num)
        dfs(nums=nums[i + 1:], target=target - curr_num, comb=comb, res=res)
        comb.pop()


if __name__ == '__main__':
    for nums, target, res in (
            ([10, 1, 2, 7, 6, 1, 5], 8, [
                [1, 1, 6],
                [1, 2, 5],
                [1, 7],
                [2, 6]
            ]),
            #####
            ([2, 5, 2, 1, 2], 5, [
                [1, 2, 2],
                [5]
            ]),
    ):
        assert (actual := combination_sum_2(nums, target)) == res, actual
