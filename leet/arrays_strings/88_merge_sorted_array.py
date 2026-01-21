def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    m_ptr = m - 1
    n_ptr = n - 1
    res_ptr = len(nums1) - 1
    while m_ptr >= 0 and n_ptr >= 0:
        if nums1[m_ptr] > nums2[n_ptr]:
            nums1[res_ptr] = nums1[m_ptr]
            m_ptr -= 1
        else:
            nums1[res_ptr] = nums2[n_ptr]
            n_ptr -= 1
        res_ptr -= 1

    # NB: we only need to continue looping through the second array if we still haven't reached the zeroth index
    # There is no need to keep looping through the first array as we updating it in place
    while n_ptr >= 0:
        nums1[res_ptr] = nums2[n_ptr]
        n_ptr -= 1
        res_ptr -= 1


if __name__ == "__main__":
    for nums1, m, nums2, n, res in (
            (
                    [1, 2, 3, 0, 0, 0], 3,
                    [2, 5, 6], 3,
                    [1, 2, 2, 3, 5, 6]
            ),
            (
                    [2, 5, 6, 0, 0, 0], 3,
                    [1, 2, 3], 3,
                    [1, 2, 2, 3, 5, 6]
            ),
            ([1], 1, [], 0, [1]),
            ([0], 0, [1], 1, [1])
    ):
        merge(nums1, m, nums2, n)
        assert nums1 == res, f"{nums1} != {res}"
