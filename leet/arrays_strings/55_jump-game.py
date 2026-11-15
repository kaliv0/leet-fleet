# 55. Jump Game


def can_jump(nums: list[int]) -> bool:
    reachable = 0
    for i, n in enumerate(nums):
        if i > reachable:
            return False
        reachable = max(reachable, (i + n))
    return True


if __name__ == "__main__":
    for nums, result in (
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ):
        assert (actual := can_jump(nums)) == result, actual
