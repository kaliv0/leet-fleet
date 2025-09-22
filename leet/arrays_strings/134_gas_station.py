# 134. Gas Station

def can_complete_circuit(gas, cost):
    total_tank = 0
    tank = 0
    start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        total_tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    if total_tank < 0:
        return -1
    return start


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
    ]

    for gas, cost, result in cases:
        assert (actual := can_complete_circuit(gas, cost)) == result, \
            f"{actual} != {result}, {gas=}, {cost=}"
