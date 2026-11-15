# 11. Container With Most Water


def max_area(height: list[int]) -> int:
    area = 0
    left = 0
    right = len(height) - 1

    while left < right:
        # calculate area at each step
        local_height = min(height[left], height[right])
        local_width = right - left
        local_area = local_height * local_width
        area = max(area, local_area)

        # how we decide to proceed? NB: we keep the taller 'height'
        # -> increased chance to have a bigger area on next iteration
        if height[left] < height[right]:
            left += 1
        elif height[right] <= height[left]:
            right -= 1

    return area


if __name__ == "__main__":
    cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 7, 2, 5, 4, 7, 3, 6], 36),
        ([2, 2, 2], 4),
        ([1, 1], 1),
    ]

    for height, result in cases:
        assert (actual := max_area(height)) == result, actual
