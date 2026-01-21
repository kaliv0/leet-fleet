# 169. Majority Element

def majority_element(nums: list[int]) -> int:
    # Boyer-Moore's algorithm
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        else:
            if candidate == num:
                count += 1
            else:
                count -= 1

    return candidate


def majority_element_naive(nums: list[int]) -> int:
    from collections import defaultdict

    half_size = len(nums) // 2
    count_map = defaultdict(int)
    res = 0
    for n in nums:
        count_map[n] += 1
        if count_map[n] > half_size:
            res = n
            break
    return res


if __name__ == '__main__':
    for nums, res in (
            ([3, 2, 3], 3),
            ([2, 2, 1, 1, 1, 2, 2], 2)
    ):
        assert (act := majority_element(nums)) == res, f'expected: {res} != actual: {act}'
