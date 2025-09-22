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
    assert car_fleet(target = 10, position = [1,4], speed = [3,2]) == 1
    assert car_fleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]) == 3