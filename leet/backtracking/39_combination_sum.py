def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    stack = []

    def _backtrack(target, start):
        # base case -> target <= 0
        if target == 0:
            res.append(list(stack))
            return
        elif target < 0:
            return

        for i in range(start, len(candidates)):
            curr_num = candidates[i]
            # register curr_num to come back to it later
            stack.append(curr_num)
            # NB: use smaller target (excluding nums we already have in the stack) wile exploring further
            _backtrack(target - curr_num, i)
            # go back
            stack.pop()

    _backtrack(target, 0)
    return res


if __name__ == '__main__':
    cases = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, [])
    ]

    for nums, target, res in cases:
        assert (actual := combination_sum(nums, target)) == res, actual
