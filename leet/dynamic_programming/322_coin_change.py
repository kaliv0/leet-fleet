# 322. Coin Change

# top-down
def coin_change(coins: list[int], amount: int) -> int:
    res = dp(coins, amount, {})
    return -1 if res == float('inf') else res


def dp(coins, amount, memo):
    if amount == 0:
        return 0

    if amount not in memo:
        min_coins = float('inf')
        for coin in coins:
            if coin <= amount:
                min_coins = min(1 + dp(coins, amount - coin, memo), min_coins)
        memo[amount] = min_coins

    return memo[amount]


# bottom-up
def coin_change_alt(coins: list[int], amount: int) -> int:
    dp_ = [float('inf')] * (amount + 1)
    dp_[0] = 0  # base case if val == coin

    for coin in coins:
        for val in range(1, len(dp_)):
            if coin <= val:
                dp_[val] = min(1 + dp_[val - coin], dp_[val])

    return -1 if dp_[amount] == float('inf') else dp_[amount]


if __name__ == "__main__":
    for coins, amount, res in (
            ([1, 2, 5], 11, 3),
            ([186, 419, 83, 408], 6242, 19),
            ([2], 3, -1),
            ([1], 0, 0),
    ):
        assert (actual := coin_change_alt(coins, amount)) == res, f"{actual} != {res}"
