# 19. Remove Nth Node From End of List
from typing import Optional

from leet.linked_lists.utils import ListNode, traverse_list


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast = head
    slow = head

    for _ in range(0, n):
        fast = fast.next

    if fast is None:
        return slow.next  # or head.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head


if __name__ == "__main__":
    list_1 = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=3,
                next=ListNode(
                    val=4,
                    next=ListNode(
                        val=5,
                    )
                )
            )
        )
    )
    assert traverse_list(remove_nth_from_end(list_1, n=2)) == [1, 2, 3, 5]

    list_2 = ListNode(val=1)
    assert traverse_list(remove_nth_from_end(list_2, n=1)) == []

    list_3 = ListNode(val=1, next=ListNode(val=2))
    assert traverse_list(remove_nth_from_end(list_3, n=2)) == [2]
