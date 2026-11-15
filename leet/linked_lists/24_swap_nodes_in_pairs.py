# 24. Swap Nodes in Pairs

from leet.linked_lists.utils import ListNode, build_list, traverse_list


def swap_pairs(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return head

    dummy = ListNode(next=head)
    prev_left = dummy
    left = head
    right = head.next

    while right:
        # swap
        prev_left.next = right
        left.next = right.next
        right.next = left
        # move pointers
        prev_left = left
        left = left.next
        right = left and left.next

    return dummy.next


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([1, 2, 3], [2, 1, 3]),
        ([], []),
        ([1], [1]),
    ]

    for inp, result in cases:
        assert (actual := traverse_list(swap_pairs(build_list(inp)))) == result, actual
