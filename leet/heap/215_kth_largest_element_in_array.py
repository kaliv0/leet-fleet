# 215. Kth Largest Element in an Array
import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    # use max heap to find largest elements
    # use negative nums as a work around since in python3.13 max heap is not available
    nums = [-n for n in nums]
    heapq.heapify(nums)
    for _ in range(k - 1):
        heapq.heappop(nums)
    return -heapq.heappop(nums)


if __name__ == "__main__":
    for nums, k, res in (
            ([3, 2, 1, 5, 6, 4], 2, 5),
            ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4)
    ):
        assert (actual := find_kth_largest(nums, k)) == res, actual
