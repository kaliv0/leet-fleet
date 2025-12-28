# 219. Contains Duplicate II

def contains_nearby_duplicate(nums, k):
    hashmap = {}
    for i, num in enumerate(nums):
        if num in hashmap:
            j = hashmap[num]
            if i != j and abs(i - j) <= k:
                return True
        # if num is already in the map, by updating the index we guarantee that
        # abs(i - j) will be smaller than k if another occurrence of num is found
        hashmap[num] = i
    return False


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
    ]

    for nums, k, result in cases:
        assert (actual := contains_nearby_duplicate(nums, k)) == result, \
            f"{actual} != {result}, {nums=}, {k=}"
