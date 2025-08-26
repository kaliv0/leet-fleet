# 61. Rotate List
from typing import Optional

from leet.linked_lists.utils import ListNode, traverse_list


def rotate_right(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if head is None or head.next is None or k == 0:
        return head

    # find list length
    curr = head
    list_len = 1
    while curr and curr.next:
        curr = curr.next
        list_len += 1
    # readjust k
    k = k % list_len
    if k == 0:
        return head

    dummy = ListNode()
    dummy.next = head
    fast = head
    slow = dummy
    counter = 1
    # find point to break list in two
    while fast.next:
        fast = fast.next
        counter += 1
        if counter > k:
            slow = slow.next
    # detach sib-list
    new_head = slow.next
    slow.next = None
    # append in front
    second = dummy.next
    dummy.next = new_head
    # find last node of new_head to attach to second sub_list
    while new_head and new_head.next:
        new_head = new_head.next
    new_head.next = second

    return dummy.next


def rotate_right_brute_force(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    dummy = ListNode()
    dummy.next = head

    for _ in range(k):
        # find tail
        curr = dummy.next
        while curr.next.next:
            curr = curr.next
        # rotate -> detach tail, insert between dummy and head
        tmp = curr.next
        curr.next = None
        second = dummy.next
        dummy.next = tmp
        tmp.next = second

    return dummy.next


if __name__ == "__main__":
    list_1 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3, next=ListNode(
                    val=4, next=ListNode(
                        val=5)))))
    # assert traverse_list(rotate_right_brute_force(list_1, 2)) == [4, 5, 1, 2, 3]
    assert traverse_list(rotate_right(list_1, 2)) == [4, 5, 1, 2, 3]

    list_2 = ListNode(
        val=0, next=ListNode(
            val=1, next=ListNode(
                val=2)))
    # assert traverse_list(rotate_right_brute_force(list_2, 4)) == [2, 0, 1]
    assert traverse_list(rotate_right(list_2, 4)) == [2, 0, 1]

    list_3 = ListNode(val=1, next=ListNode(val=2))
    # assert traverse_list(rotate_right_brute_force(list_3, 1)) == [2, 1]
    assert traverse_list(rotate_right(list_3, 1)) == [2, 1]

    list_4 = ListNode(val=1, next=ListNode(val=2))
    assert traverse_list(rotate_right(list_4, 2)) == [1, 2]

    # assert traverse_list(rotate_right_brute_force(None, 2)) == []
    assert traverse_list(rotate_right(None, 2)) == []

    # assert traverse_list(rotate_right_brute_force(ListNode(val=1), 4)) == [1]
    assert traverse_list(rotate_right(ListNode(val=1), 4)) == [1]

    assert traverse_list(rotate_right(ListNode(val=1), 0)) == [1]
