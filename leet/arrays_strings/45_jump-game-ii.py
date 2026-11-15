# 45. Jump Game II


def jump(nums: list[int]) -> int:
    jumps = 0
    reachable = 0
    position = 0
    for i in range(len(nums) - 1):
        reachable = max(reachable, i + nums[i])
        if i == position:
            position = reachable
            jumps += 1
    return jumps


if __name__ == "__main__":
    cases = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([2, 3, 1], 1),
        ([1, 1, 3, 1, 1], 3),
    ]

    for nums, result in cases:
        assert (actual := jump(nums)) == result, actual
