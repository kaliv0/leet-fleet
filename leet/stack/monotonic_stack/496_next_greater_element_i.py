# 496. Next Greater Element I


def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    # create map of all elements in nums2 with corresponding NGE
    ngt_map = {}
    stack = []
    for n in nums2:
        while stack and stack[-1] < n:
            ngt_map[stack.pop()] = n
        stack.append(n)

    # loop through num1 and map -> build and return result
    return [ngt_map.get(n, -1) for n in nums1]


if __name__ == '__main__':
    for nums1, nums2, res in (
            ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
            ([2, 4], [1, 2, 3, 4], [3, -1])
    ):
        assert (actual := next_greater_element(nums1, nums2)) == res, actual
