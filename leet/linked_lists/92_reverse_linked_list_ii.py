# 92. Reverse Linked List II

from leet.linked_lists.utils import build_list, traverse_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_between(head: ListNode | None, left: int, right: int) -> ListNode | None:
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
    cases = [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([1, 2, 3, 4, 5], 1, 4, [4, 3, 2, 1, 5]),
        ([1, 2, 3, 4, 5], 2, 5, [1, 5, 4, 3, 2]),
        ([1, 2, 3, 4, 5], 1, 5, [5, 4, 3, 2, 1]),
        ([5], 1, 1, [5]),
        ([], 1, 3, []),
    ]

    for inp, left, right, result in cases:
        assert (
            actual := traverse_list(reverse_between(build_list(inp), left, right))
        ) == result, actual
