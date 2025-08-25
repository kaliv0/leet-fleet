from typing import Optional

from leet.linked_lists.utils import DoublyListNode, traverse_list, traverse_back


def reverse_list(head: Optional[DoublyListNode]) -> Optional[DoublyListNode]:
    if not head or not head.next:
        return head

    prev = None
    curr = head
    next = curr.next

    while curr.next:
        # reverse
        curr.next = prev
        curr.prev = next
        # move pointers
        prev = curr
        curr = next
        next = curr.next

    curr.next = prev
    curr.prev = None
    return curr


if __name__ == "__main__":
    # case_1
    one = DoublyListNode(val=1)  # head
    two = DoublyListNode(val=2, prev=one)
    three = DoublyListNode(val=3, prev=two)
    four = DoublyListNode(val=4, prev=three)
    five = DoublyListNode(val=5, prev=four)  # tail

    one.next = two
    two.next = three
    three.next = four
    four.next = five

    reversed = reverse_list(one)
    assert traverse_list(reversed) == [5, 4, 3, 2, 1]
    assert traverse_back(reversed) == [1, 2, 3, 4, 5]

    # case_2
    one = DoublyListNode(val=1)  # head
    two = DoublyListNode(val=2, prev=one)  # tail
    one.next = two

    reversed = reverse_list(one)
    assert traverse_list(reversed) == [2, 1]
    assert traverse_back(reversed) == [1, 2]

    # case_3
    one = DoublyListNode(val=1)  # head & tail
    assert traverse_list(reverse_list(one)) == [1]

    # case_4
    assert traverse_list(reverse_list(None)) == []
