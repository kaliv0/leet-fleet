# 518. Coin Change II
def change(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1  # used for base case

    for coin in coins:
        for val in range(coin, len(dp)):
            dp[val] += dp[val - coin]
            # if val == coin -> dp[val - coin] will give us 1 (dp[0]) -> base case - use coin to create amount
            # if val > coin -> we need to use the coin + extra value -> reuse dp record for that extra value (dp[val - coin])

    return dp[amount]


if __name__ == "__main__":
    for amount, coins, res in (
            (5, [1, 2, 5], 4),
            (3, [2], 0),
            (10, [10], 1)
    ):
        assert (actual := change(amount, coins)) == res, f"{actual} != {res}"
