# 328. Odd Even Linked List

from typing import Optional

from leet.linked_lists.utils import ListNode, traverse_list


def odd_even_dance(head):
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    new_head = even

    while even and even.next:
        # skip/ remove node, go to next location
        odd.next = odd.next.next
        odd = odd.next
        # same choreography
        even.next = even.next.next
        even = even.next
    # attach both lists
    odd.next = new_head
    return head


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    curr = head

    even = ListNode()
    other = even
    while curr.next and curr.next.next:
        # detach even node from main list
        tmp = curr.next
        # attach prev to next odd
        curr.next = curr.next.next
        # attach even to new list
        other.next = tmp
        # move pointers
        curr = curr.next
        other = other.next

    # detach last one
    tmp = curr.next
    other.next = tmp
    # combine both lists
    curr.next = even.next

    return head


if __name__ == "__main__":
    list_1 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3, next=ListNode(
                    val=4, next=ListNode(
                        val=5, next=ListNode(
                            val=6))))))
    # assert traverse_list(odd_even_list(list_1)) == [1, 3, 5, 2, 4, 6]
    assert traverse_list(odd_even_dance(list_1)) == [1, 3, 5, 2, 4, 6]

    list_2 = ListNode(
        val=2, next=ListNode(
            val=1, next=ListNode(
                val=3, next=ListNode(
                    val=5, next=ListNode(
                        val=6, next=ListNode(
                            val=4, next=ListNode(
                                val=7)))))))
    # assert traverse_list(odd_even_list(list_2)) == [2, 3, 6, 7, 1, 5, 4]
    assert traverse_list(odd_even_dance(list_2)) == [2, 3, 6, 7, 1, 5, 4]

    list_3 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3, next=ListNode(
                    val=4, next=ListNode(
                        val=5)))))
    # assert traverse_list(odd_even_list(list_3)) == [1, 3, 5, 2, 4]
    assert traverse_list(odd_even_dance(list_3)) == [1, 3, 5, 2, 4]

    list_4 = ListNode(val=1, next=ListNode(val=2))
    # assert traverse_list(odd_even_list(list_4)) == [1, 2]
    assert traverse_list(odd_even_dance(list_4)) == [1, 2]

    # assert traverse_list(odd_even_list(ListNode(val=1))) == [1]
    assert traverse_list(odd_even_dance(ListNode(val=1))) == [1]

    # assert traverse_list(odd_even_list(None)) == []
    assert traverse_list(odd_even_dance(None)) == []
