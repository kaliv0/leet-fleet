# 503. Next Greater Element II
def next_greater_elements(nums: list[int]) -> list[int]:
    res = [0] * len(nums)
    stack = []
    # loop twice since it's a circular array -> second time adjusts results
    for t in range(2):
        for i in range(len(nums) - 1, -1, -1):
            # build decreasing monotonic stack
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            # update result before adding new element to stack
            res[i] = stack[-1] if stack else -1
            stack.append(nums[i])

    return res


if __name__ == '__main__':
    for nums, res in (
            ([1, 2, 1], [2, -1, 2]),
            ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
    ):
        assert (actual := next_greater_elements(nums)) == res, actual
