# 24. Swap Nodes in Pairs
from typing import Optional

from leet.linked_lists.utils import ListNode, traverse_list


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
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
    list_1 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3, next=ListNode(
                    val=4))))
    assert traverse_list(swap_pairs(list_1)) == [2, 1, 4, 3]

    list_2 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3)))
    assert traverse_list(swap_pairs(list_2)) == [2, 1, 3]

    assert traverse_list(swap_pairs(None)) == []
    assert traverse_list(swap_pairs(ListNode(1))) == [1]
