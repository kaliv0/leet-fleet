# 135. Candy
def candy(ratings: list[int]) -> int:
    # all children receive at least one candy
    candies = [1] * len(ratings)

    # traverse twice-> on first pass give one more candy than the previous child if curr rating is higher
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # second pass (backwards) to adjust candies
    for i in range(len(ratings) - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            # give more candies if rating is higher and the amount needs to be adjusted (!)
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


if __name__ == "__main__":
    for ratings, res in (
            ([1, 0, 2], 5),
            ([1, 2, 2], 4),
            ([1, 3, 4, 5, 2], 11),
    ):
        assert (actual := candy(ratings)) == res, actual
