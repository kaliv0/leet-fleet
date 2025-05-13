def binary_search(arr, num, offset=0):
    if not arr:
        return -1

    curr_mid = len(arr) // 2
    curr_num = arr[curr_mid]
    if curr_num == num:
        return curr_mid + offset

    if curr_num > num:
        return binary_search(arr[0:curr_mid], num, offset)

    return binary_search(arr[curr_mid + 1:], num, curr_mid + 1)


def bin_search(nums, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if nums[mid] > target:
        return bin_search(nums, target, left=0, right=mid - 1)
    return bin_search(nums, target, left=mid + 1, right=right)


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5, 6], 2, 1),
        ([], 2, -1),
        ([1], 1, 0),
        ([1], 2, -1),
        ([1, 2, 3, 4, 5, 6, 7], 2, 1),
        ([1, 2, 3, 4, 5, 6], -2, -1),
        ([1, 2, 3, 4, 5, 6], 6, 5)
    ]

    for arr, num, res in cases:
        assert (actual := bin_search(arr, num, 0, len(arr) - 1)) == res, f"{actual} != {res}"
        # assert (actual := binary_search(arr, num)) == res, f"{actual} != {res}"
