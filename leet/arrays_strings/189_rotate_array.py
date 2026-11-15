# 189. Rotate Array


def rotate(nums: list[int], k: int) -> None:
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]


if __name__ == "__main__":
    for nums, k, result in (
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1, 2], 3, [2, 1]),
    ):
        rotate(nums, k)
        assert nums == result, nums
