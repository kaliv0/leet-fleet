# 735. Asteroid Collision


def asteroid_collision(asteroids: list[int]) -> list[int]:
    stack = []
    for a in asteroids:
        while stack and stack[-1] > 0 > a:
            diff = stack[-1] - abs(a)
            if diff > 0:
                a = 0
            elif diff == 0:
                stack.pop()
                a = 0
            else:
                stack.pop()
        if a:
            stack.append(a)
    return stack


if __name__ == "__main__":
    cases = [
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([-2, -1, 1, 2], [-2, -1, 1, 2]),
    ]

    for asteroids, result in cases:
        assert (actual := asteroid_collision(asteroids)) == result, actual
