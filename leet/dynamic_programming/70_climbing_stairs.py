# 70. Climbing Stairs

memo = {
    0: 0,
    1: 1,
    2: 2
}


def climb_stairs(n):
    if n in memo:
        return memo[n]
    if n - 1 not in memo:
        memo[n - 1] = climb_stairs(n - 1)
    if n - 2 not in memo:
        memo[n - 2] = climb_stairs(n - 2)
    return memo[n - 1] + memo[n - 2]


if __name__ == "__main__":
    cases = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (11, 144)
    ]

    for n, res in cases:
        assert (actual := climb_stairs(n)) == res, \
            f"{actual} != {res}, {n=}"
