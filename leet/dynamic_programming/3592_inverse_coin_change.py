# 3592. Inverse Coin Change
def find_coins(num_ways: list[int]) -> list[int]:
    ...


if __name__ == "__main__":
    for ways, coins in (
            ([0, 1, 0, 2, 0, 3, 0, 4, 0, 5], [2, 4, 6]),
            ([1, 2, 2, 3, 4], [1, 2, 5]),
            ([1, 2, 3, 4, 15], []),
    ):
        assert (actual := find_coins(ways)) == coins, f"{actual} != {coins}"
