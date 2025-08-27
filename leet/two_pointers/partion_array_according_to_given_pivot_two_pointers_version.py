# 2161. Partition Array According to Given Pivot
def pivot_array_two_pointers(nums: list[int], pivot: int) -> list[int]:
    result = [0] * len(nums)
    left = l_ans = 0
    right = r_ans = len(nums) - 1
    while left < len(nums) or right >= 0:
        if nums[left] < pivot:
            # add number & move result pointer
            result[l_ans] = nums[left]
            l_ans += 1
        if nums[right] > pivot:
            result[r_ans] = nums[right]
            r_ans -= 1
        # move pointers on nums arr
        left += 1
        right -= 1

    # add nums = pivot
    while l_ans <= r_ans:
        result[l_ans] = pivot
        l_ans += 1

    return result


if __name__ == "__main__":
    assert pivot_array_two_pointers(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10) == [9, 5, 3, 10, 10, 12, 14]
    assert pivot_array_two_pointers(nums=[-3, 4, 3, 2], pivot=2) == [-3, 2, 4, 3]
