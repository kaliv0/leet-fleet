# 922. Sort Array By Parity II
def sort_array_by_parity_ii(nums: list[int]) -> list[int]:
    # sort in place
    left = 0
    while left < len(nums):
        # both num value and index are even or odd
        if nums[left] % 2 == left % 2:
            left += 1
            continue

        # search value on right side to swap with
        right = left + 1
        while right < len(nums):
            if nums[right] % 2 == left % 2:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                break
            right += 1

    return nums


if __name__ == "__main__":
    assert sort_array_by_parity_ii([4, 2, 5, 7]) in ([4, 7, 2, 5], [2, 5, 4, 7], [2, 7, 4, 5], [4, 5, 2, 7])
    assert sort_array_by_parity_ii([2, 3]) == [2, 3]
    assert sort_array_by_parity_ii([]) == []
