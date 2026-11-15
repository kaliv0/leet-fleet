# 21. Best Time to Buy and Sell Stock


def max_profit(prices: list[int]) -> int:
    profit = 0
    lowest = 0
    runner = 1
    while runner < len(prices):
        if prices[runner] < prices[lowest]:
            lowest = runner
        else:
            profit = max(profit, prices[runner] - prices[lowest])
        runner += 1
    return profit


if __name__ == "__main__":
    for prices, result in (
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
    ):
        assert (actual := max_profit(prices)) == result, actual
