# 373. Find K Pairs with Smallest Sums
import heapq


def k_smallest_pairs_opt(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    pairs = []
    # NB: nums1 are already sorted asc -> we add at most k elements initially
    for i in range(min(len(nums1), k)):
        heapq.heappush(pairs, (nums1[i] + nums2[0], i, 0))

    res = []
    while k > 0 and pairs:
        curr_sum, i, j = heapq.heappop(pairs)
        res.append([nums1[i], nums2[j]])
        # we add other pairs dynamically after popping from heap to keep memory allocation low
        if j + 1 < len(nums2):
            heapq.heappush(pairs, (nums1[i] + nums2[j + 1], i, j + 1))
        k -= 1

    return res


############################
def k_smallest_pairs_alt(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    pairs = [(i + j, [i, j]) for i in nums1 for j in nums2]
    heapq.heapify(pairs)
    return [heapq.heappop(pairs)[1] for _ in range(k)]


############################
def k_smallest_pairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    # prepare all possible pairs
    pairs = []
    for i in nums1:
        for j in nums2:
            pairs.append(Pair(i, j))

    heapq.heapify(pairs)

    # heapify map and pop first k elements
    res = []
    for _ in range(k):
        min_pair = heapq.heappop(pairs)
        res.append([min_pair.a, min_pair.b])

    return res


class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __lt__(self, other):
        return self.a + self.b < other.a + other.b


if __name__ == "__main__":
    for nums1, nums2, k, res in (
            ([1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]]),
            ([1, 1, 2], [1, 2, 3], 2, [[1, 1], [1, 1]]),
    ):
        assert (actual := k_smallest_pairs_opt(nums1, nums2, k)) == res, actual
