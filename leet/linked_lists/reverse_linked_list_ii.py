from typing import Optional

from leet.linked_lists.utils import traverse_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head or left == right:
        return head

    # traverse to left_pos
    counter = 1
    prev = None
    curr = head
    while counter < left:
        prev = curr
        curr = curr.next
        counter += 1

    # reverse
    new_head, right_node = reverse_list(curr, left, right)
    # join left side
    if prev:
        prev.next = new_head
    else:
        # in case left points to head in the beginning
        head = new_head

    # join right side
    curr = new_head
    while counter < right:
        curr = curr.next
        counter += 1
    curr.next = right_node
    return head


def reverse_list(head, left, right):
    if not head or not head.next:
        return head

    prev = None
    curr = head
    counter = 0
    while curr.next and counter < right - left:
        # reverse
        temp = curr.next
        curr.next = prev
        # move pointers
        prev = curr
        curr = temp
        counter += 1
    # adjust tail and return as new head
    right_node = curr.next
    curr.next = prev
    return curr, right_node


if __name__ == "__main__":
    # case_1 -> range in middle
    five = ListNode(val=5, next=None)  # tail
    four = ListNode(val=4, next=five)
    three = ListNode(val=3, next=four)
    two = ListNode(val=2, next=three)
    one = ListNode(val=1, next=two)  # head

    left = 2
    right = 4
    assert traverse_list(reverse_between(one, left, right)) == [1, 4, 3, 2, 5]

    # case_2 -> left side to middle
    five = ListNode(val=5, next=None)  # tail
    four = ListNode(val=4, next=five)
    three = ListNode(val=3, next=four)
    two = ListNode(val=2, next=three)
    one = ListNode(val=1, next=two)  # head

    left = 1
    right = 4
    assert traverse_list(reverse_between(one, left, right)) == [4, 3, 2, 1, 5]

    # case_3 -> middle to right side
    five = ListNode(val=5, next=None)  # tail
    four = ListNode(val=4, next=five)
    three = ListNode(val=3, next=four)
    two = ListNode(val=2, next=three)
    one = ListNode(val=1, next=two)  # head

    left = 2
    right = 5
    assert traverse_list(reverse_between(one, left, right)) == [1, 5, 4, 3, 2]

    # case_4 -> full reversal
    five = ListNode(val=5, next=None)  # tail
    four = ListNode(val=4, next=five)
    three = ListNode(val=3, next=four)
    two = ListNode(val=2, next=three)
    one = ListNode(val=1, next=two)  # head

    left = 1
    right = 5
    assert traverse_list(reverse_between(one, left, right)) == [5, 4, 3, 2, 1]

    # case_5
    one = ListNode(val=5, next=None)  # head & tail
    left = 1
    right = 1
    assert traverse_list(reverse_between(one, left, right)) == [5]

    # case_6
    assert traverse_list(res := reverse_between(None, 1, 3)) == []
