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



if __name__ == '__main__':
    assert min_eating_speed(piles=[3, 6, 7, 11], h=8) == 4
    assert min_eating_speed(piles=[30, 11, 23, 4, 20], h=5) == 30
    assert min_eating_speed(piles=[30, 11, 23, 4, 20], h=6) == 23
