# 1721. Swapping Nodes in a Linked List
from typing import Optional

from leet.linked_lists.utils import ListNode, traverse_list


def swap_nodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    dummy = ListNode()
    dummy.next = head
    # pre_left, pre_right = find_left_right_unoptimized(dummy, head, k)
    curr = dummy
    for _ in range(1, k):
        curr = curr.next

    pre_left = curr

    pre_right = dummy
    while curr.next.next:
        curr = curr.next
        pre_right = pre_right.next

    # swap left and right
    left = pre_left.next
    right = pre_right.next

    # swapping this way won't be possible e.g. in Java
    pre_left.next, pre_right.next = right, left
    left.next, right.next = right.next, left.next
    return dummy.next


def find_left_right_unoptimized(dummy, head, k):
    # find node before right target
    pre_right = dummy
    curr = head
    counter = 0
    while curr:
        curr = curr.next
        counter += 1
        if counter >= k + 1:
            pre_right = pre_right.next
    # find node before left target
    pre_left = dummy
    counter = 0
    while counter < k - 1:
        pre_left = pre_left.next
        counter += 1
    return pre_left, pre_right


if __name__ == "__main__":
    list_1 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3, next=ListNode(
                    val=4, next=ListNode(
                        val=5)))))
    assert traverse_list(swap_nodes(list_1, 2)) == [1, 4, 3, 2, 5]

    list_2 = ListNode(
        val=7, next=ListNode(
            val=9, next=ListNode(
                val=6, next=ListNode(
                    val=6, next=ListNode(
                        val=7, next=ListNode(
                            val=8, next=ListNode(
                                val=3, next=ListNode(
                                    val=0, next=ListNode(
                                        val=9, next=ListNode(
                                            val=5))))))))))
    assert traverse_list(swap_nodes(list_2, 5)) == [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]

    list_3 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3, next=ListNode(
                    val=4, next=ListNode(
                        val=5)))))
    assert traverse_list(swap_nodes(list_3, 1)) == [5, 2, 3, 4, 1]
