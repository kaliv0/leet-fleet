def is_happy(n: int) -> bool:
    memo = set()
    while True:
        n = split_digits(n)
        if n < 10:
            if n == 1:
                return True
            if n in memo:
                return False
            memo.add(n)


def split_digits(n):
    res = 0
    while n >= 10:
        last_digit = n % 10
        res += last_digit ** 2
        n //= 10
    res += n ** 2
    return res


if __name__ == "__main__":
    cases = [
        (19, True),
        (2, False),
        (7, True),
        (1111111, True),
    ]

    for num, res in cases:
        assert (actual := is_happy(num)) == res, \
            f"{actual} != {res}, {num=}"
