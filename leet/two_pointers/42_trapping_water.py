# 42. Trapping Rain Water
def trap(height: list[int]) -> int:
    max_water = 0
    max_left = 0
    max_right = 0

    left = 0
    right = len(height) - 1
    while left < right:
        curr_left = height[left]
        curr_right = height[right]

        if curr_left <= curr_right:
            # NG: we trap water only if curr_height is smaller than curr max_height
            # otherwise we update max_height
            if curr_left < max_left:
                max_water += max_left - curr_left
            else:
                max_left = curr_left
            left += 1
        elif curr_left > curr_right:
            if curr_right < max_right:
                max_water += max_right - curr_right
            else:
                max_right = curr_right
            right -= 1

    return max_water


if __name__ == "__main__":
    for nums, res in (
            ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
            ([4, 2, 0, 3, 2, 5], 9)
    ):
        assert (actual := trap(nums)) == res, actual
