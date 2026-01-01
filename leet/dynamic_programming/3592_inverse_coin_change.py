# 3592. Inverse Coin Change
def find_coins(num_ways: list[int]) -> list[int]:
    num_ways = [1] + num_ways  # add base case for zero
    res = []

    for i in range(1, len(num_ways)):
        if num_ways[i] > 1:
            return []
        if num_ways[i] == 0:
            continue

        res.append(i)
        for j in range(len(num_ways) - 1, i - 1, -1):
            num_ways[j] -= num_ways[j - i]
            if num_ways[j] < 0:
                return []
    return res


if __name__ == "__main__":
    for ways, coins in (
            ([0, 1, 0, 2, 0, 3, 0, 4, 0, 5], [2, 4, 6]),
            ([1, 2, 2, 3, 4], [1, 2, 5]),
            ([1, 2, 3, 4, 15], []),
    ):
        assert (actual := find_coins(ways)) == coins, f"{actual} != {coins}"
