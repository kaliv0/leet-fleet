# 875. Koko Eating Bananas
import math


def min_eating_speed(piles: list[int], h: int) -> int:
    left = 1
    right = max(piles)
    result = right

    while left <= right:
        mid = (left + right) // 2

        total_time = 0
        for pile in piles:
            total_time += math.ceil(pile / mid)
        if total_time <= h:
            result = mid
            # we've found a solution, but we'll search for more optimal one
            right = mid - 1
        else:
            left = mid + 1

    return result


if __name__ == "__main__":
    for piles, h, result in (
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ):
        assert (actual := min_eating_speed(piles, h)) == result, actual
