# 876. Middle of the Linked List
from typing import Optional

from leet.linked_lists.utils import ListNode


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    fast = head
    slow = head
    while fast.next and fast.next.next:
        # when fast reaches the last node, slow will be on the middle one
        fast = fast.next.next
        slow = slow.next

    if fast.next:
        # if fast is on the penultimate node -> move slow one more mode to the right
        slow = slow.next
    return slow
