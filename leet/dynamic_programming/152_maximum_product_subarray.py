# 152. Maximum Product Subarray
def max_product(nums: list[int]) -> int:
    max_prod = nums[0]
    min_prod = nums[0]
    total_prod = nums[0]
    for n in nums[1:]:
        if n < 0:
            # if current num is negative multiplying by curr min/max prods will swap their values
            min_prod, max_prod = max_prod, min_prod
        max_prod = max(n, max_prod * n)
        min_prod = min(n, min_prod * n)
        total_prod = max(total_prod, max_prod)
    return total_prod


def max_product_alt(nums: list[int]) -> int:
    # modified Kadane's algorithm, but we traverse nums array twice so it's less efficient
    max_prod = nums[0]
    curr_prod = 1
    for n in nums:
        if curr_prod == 0:
            curr_prod = 1
        curr_prod *= n
        max_prod = max(max_prod, curr_prod)

    curr_prod = 1
    for i in range(len(nums) - 1, -1, -1):
        if curr_prod == 0:
            curr_prod = 1
        curr_prod *= nums[i]
        max_prod = max(max_prod, curr_prod)

    return max_prod


if __name__ == "__main__":
    for nums, res in (
            ([2, 3, -2, 4], 6),
            ([-2, 0, -1], 0),
            ([-3, -1, -1], 3),
            ([3, -1, 4], 4),
            ([1], 1),
    ):
        assert (actual := max_product_alt(nums)) == res, f"{actual} != {res}"
