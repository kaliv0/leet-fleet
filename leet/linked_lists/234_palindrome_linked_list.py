# 234. Palindrome Linked List
from leet.linked_lists.utils import ListNode, build_list


def is_palindrome(head):
    stack = []

    fast = head
    slow = head
    while fast.next and fast.next.next:
        stack.append(slow.val)
        fast = fast.next.next
        slow = slow.next

    if fast.next:
        stack.append(slow.val)
    slow = slow.next

    while slow:
        if slow.val != stack.pop(-1):
            return False
        slow = slow.next

    return True


if __name__ == "__main__":
    cases = [
        ([1, 2, 2, 1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3], False),
        ([0], True),
    ]

    for inp, result in cases:
        assert (actual := is_palindrome(build_list(inp))) is result, actual
