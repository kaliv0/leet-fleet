# 121. Best Time to Buy and Sell Stock


def max_profit(prices: list[int]) -> int:
    left = 0
    right = 1
    max_p = 0

    while right < len(prices):
        if (old_price := prices[left]) < (new_price := prices[right]):
            profit = new_price - old_price
            max_p = max(profit, max_p)
        else:
            left = right
        right += 1

    return max_p


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
