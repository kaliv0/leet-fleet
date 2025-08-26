# 234. Palindrome Linked List
from leet.linked_lists.utils import ListNode


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
    list_1 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=2, next=ListNode(
                    val=1
                )
            )
        )
    )
    assert is_palindrome(list_1) is True

    list_2 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3, next=ListNode(
                    val=2, next=ListNode(
                        val=1
                    )
                )
            )
        )
    )
    assert is_palindrome(list_2) is True

    list_3 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))
    assert is_palindrome(list_3) is False

    assert is_palindrome(ListNode(val=0)) is True
