# 35. Search Insert Position
def search_insert(nums: list[int], target: int) -> int:
    return bin_search(nums, target, 0, len(nums) - 1)


def bin_search(nums, target, left, right):
    if left > right:
        return left

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if nums[mid] > target:
        return bin_search(nums, target, left=0, right=mid - 1)
    return bin_search(nums, target, left=mid + 1, right=right)


if __name__ == "__main__":
    cases = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([], 0, 0)
    ]
    for nums, target, result in cases:
        assert (actual := search_insert(nums, target)) == result, \
            f"{actual} != {result}, {nums=}"
