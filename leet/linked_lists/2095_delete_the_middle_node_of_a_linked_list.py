# 2095. Delete the Middle Node of a Linked List

from leet.linked_lists.utils import ListNode, build_list, traverse_list


def delete_middle(head: ListNode | None) -> ListNode | None:
    if head.next is None:
        # only on node
        return None

    fast = head.next  # NB: strat one step ahead
    slow = head
    while fast.next and fast.next.next:
        # move twice as fast as the slow pointer
        fast = fast.next.next
        slow = slow.next
    # when fast pointer reaches the last node (number of nodes is even)
    # -> slow pointer as right before the middle one
    slow.next = slow.next.next
    return head


if __name__ == "__main__":
    cases = [
        ([1, 3, 4, 7, 1, 2, 6], [1, 3, 4, 1, 2, 6]),
        ([1, 2, 3, 4], [1, 2, 4]),
        ([2, 1], [2]),
        ([1], []),
    ]

    for inp, result in cases:
        assert (actual := traverse_list(delete_middle(build_list(inp)))) == result, (
            actual
        )
