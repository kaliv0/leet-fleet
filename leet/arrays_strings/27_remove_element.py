def remove_element(nums: list[int], val: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:  # NB left == right crucial for edge cases
        if nums[left] == val:
            if nums[right] == val:
                right -= 1
                continue
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
        left += 1

    return left


if __name__ == "__main__":
    for nums, val, k in (
            ([3, 2, 2, 3], 3, 2),  # [2,2,_,_]
            ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5),  # [0,1,4,0,3,_,_,_]
            ([1], 1, 0),
            ([1], 2, 1),
            ([3, 3], 3, 0),
            ([4, 5], 4, 1),
    ):
        assert (act := remove_element(nums, val)) == k, f"{act} != {k}, from {nums}"
