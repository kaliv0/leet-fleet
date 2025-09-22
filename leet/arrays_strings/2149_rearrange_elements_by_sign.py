# 2149. Rearrange Array Elements by Sign
def rearrange_array(nums: list[int]) -> list[int]:
    # NB: It is not required to do the modifications in-place.
    positive = []
    negative = []
    for n in nums:
        if n > 0:
            positive.append(n)
        else:
            negative.append(n)

    res = []
    for i in range(len(positive)):
        res.append(positive[i])
        res.append(negative[i])
        i += 1

    return res


def rearrange_array_opt(nums: list[int]) -> list[int]:
    res = []
    pos = neg = -1
    while pos < len(nums) - 1 and neg < len(nums) - 1:
        # find next positive number
        while pos < len(nums) - 1:
            pos += 1
            if nums[pos] > 0:
                res.append(nums[pos])
                break

        # find next negative number
        while neg < len(nums) - 1:
            neg += 1
            if nums[neg] <= 0:
                res.append(nums[neg])
                break

    return res


if __name__ == "__main__":
    assert rearrange_array_opt([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]
    assert rearrange_array_opt([-1, 1]) == [1, -1]
    assert rearrange_array_opt([2, 3, -1, -4]) == [2, -1, 3, -4]
