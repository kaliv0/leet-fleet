# 2231. Largest Number After Digit Swaps by Parity
from collections import deque


def largest_integer(num: int) -> int:
    even = []
    odd = []

    tmp = num
    arr = deque()
    while tmp > 0:
        tmp, digit = divmod(tmp, 10)
        if digit % 2 == 0:
            even.append(digit)
        else:
            odd.append(digit)
        arr.appendleft(digit)

    even.sort(reverse=True)
    odd.sort(reverse=True)

    res = 0
    even_p = odd_p = 0
    for n in arr:
        if n % 2 == 0:
            res = res * 10 + even[even_p]
            even_p += 1
        else:
            res = res * 10 + odd[odd_p]
            odd_p += 1

    return res


if __name__ == "__main__":
    for num, result in (
        (1234, 3412),
        (65875, 87655),
        (247, 427),
    ):
        assert (actual := largest_integer(num)) == result, actual
