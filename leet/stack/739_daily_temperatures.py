# 739. Daily Temperatures
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []
    for i, t, in enumerate(temperatures):
        while stack and t > stack[-1][1]:
            prev_i, prev_t = stack.pop()
            res[prev_i] = i - prev_i
        stack.append((i, t))
    return res


if __name__ == '__main__':
    assert daily_temperatures([30, 38, 30, 36, 35, 40, 28]) == [1, 4, 1, 2, 1, 0, 0]
    assert daily_temperatures([22, 21, 20]) == [0, 0, 0]
