# 853. Car Fleet


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    cars_coord = [(p, s) for p, s in zip(position, speed)]
    cars_coord.sort(reverse=True)

    stack = []
    # for p, s in cars_coord:
    #     stack.append((target - p) / s)
    #     if len(stack) > 1 and stack[-1] <= stack[-2]:
    #         stack.pop()
    # return len(stack)

    for p, s in cars_coord:
        arrival = (target - p) / s
        if not stack or arrival > stack[-1]:
            stack.append(arrival)
    return len(stack)


if __name__ == "__main__":
    for target, position, speed, result in (
        (10, [1, 4], [3, 2], 1),
        (10, [4, 1, 0, 7], [2, 2, 1, 1], 3),
    ):
        assert (actual := car_fleet(target, position, speed)) == result, actual
