# 122. Best Time to Buy and Sell Stock II


from typing import List


def max_profit(prices: List[int]) -> int:
    # result = 0
    # lowest = 0
    # highest = 0
    # for i in range(len(prices)):
    #     if prices[i] < prices[lowest]:
    #         lowest = i
    #         result -= prices[i]
    #     elif prices[i] > prices[lowest]:
    #         highest = i
    #         lowest = i
    #         result += prices[highest]
    # return result

    price_gain = []

    for idx in range(len(prices) - 1):

        if prices[idx] < prices[idx + 1]:
            price_gain.append(prices[idx + 1] - prices[idx])

    return sum(price_gain)

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    # 7

    # prices = [1, 2, 3, 4, 5]
    # 4

    # prices = [7, 6, 4, 3, 1]
    # 0

    print(max_profit(prices))
