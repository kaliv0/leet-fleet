# 141. Linked List Cycle
from typing import Optional

from leet.linked_lists.utils import ListNode


# Floyd's algorithm (Hare & Tortoise)
def has_cycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

    #### alternatively ####
    # slow = fast = head
    # while fast and fast.next:
    #     slow = slow.next
    #     fast = fast.next.next
    #     if slow == fast:
    #         return True
    #
    # return False


def has_cycle_alt(head: Optional[ListNode]) -> bool:
    if head is None:
        return False

    visited = set()
    while head:
        if head in visited:
            return True
        visited.add(head)
        head = head.next

    return False
