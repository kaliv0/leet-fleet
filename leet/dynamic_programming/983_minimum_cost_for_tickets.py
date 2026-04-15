def min_cost_tickets(days: list[int], costs: list[int]) -> int:
    dp = [0] * (days[-1] + 1)

    days_it = iter(days)
    travel_day = next(days_it)

    for i in range(1, len(dp)):
        if i < travel_day:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(
                dp[i - 1] + costs[0],
                min(
                    (dp[max(0, i - 7)] + costs[1]),
                    (dp[max(0, i - 30)] + costs[2])
                )
            )
            travel_day = next(days_it, None)

    return dp[-1]


if __name__ == '__main__':
    for idx, (days, costs, res) in enumerate((
            ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17)
    )):
        assert (act := min_cost_tickets(days, costs)) == res, f"{act} != {res}, {idx=}"
