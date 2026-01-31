# 142. Linked List Cycle II
from typing import Optional

from leet.linked_lists.utils import ListNode


# Floyd's
def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    # detect cycle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    # find starting point
    # NB: The distance from the head to the start of the cycle equals
    # the distance the slow pointer has left to traverse after detection.
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast


def detect_cycle_alt(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    visited = set()
    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next

    return None
