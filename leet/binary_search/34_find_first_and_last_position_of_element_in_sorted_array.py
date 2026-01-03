# 34. Find First and Last Position of Element in Sorted Array
def search_range(nums: list[int], target: int) -> list[int]:
    lower_bound = _bs_lower(nums, target)
    upper_bound = _bs_upper(nums, target)
    return [lower_bound, upper_bound]


def _bs_lower(nums, target):
    left = 0
    right = len(nums)
    ans = -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            ans = mid  # temporary result -> keep searching to the left
            right = mid
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return ans


def _bs_upper(nums, target):
    left = 0
    right = len(nums)
    ans = -1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            ans = mid  # temporary result -> keep searching to the right
            left = mid + 1
        elif nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return ans


if __name__ == "__main__":
    for nums, target, res in (
            ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
            ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
            ([], 0, [-1, -1]),
    ):
        assert (actual := search_range(nums, target)) == res, actual
