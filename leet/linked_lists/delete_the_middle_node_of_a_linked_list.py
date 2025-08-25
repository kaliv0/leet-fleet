# 2095. Delete the Middle Node of a Linked List
from typing import Optional

from leet.linked_lists.utils import ListNode, traverse_list


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    if head.next is None:
        # only on node
        return None

    fast = head.next  # NB: strat one step ahead
    slow = head
    while fast.next and fast.next.next:
        # move twice as fast as the slow pointer
        fast = fast.next.next
        slow = slow.next
    # when fast pointer reaches the last node -> slow pointer as right before the middle one
    slow.next = slow.next.next
    return head


if __name__ == "__main__":
    list_1 = ListNode(
        val=1,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4,
                next=ListNode(
                    val=7,
                    next=ListNode(
                        val=1,
                        next=ListNode(
                            val=2,
                            next=ListNode(
                                val=6,
                            )
                        )
                    )
                )
            )
        )
    )
    assert traverse_list(delete_middle(list_1)) == [1, 3, 4, 1, 2, 6]

    list_2 = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=3,
                next=ListNode(
                    val=4,
                )
            )
        )
    )
    assert traverse_list(delete_middle(list_2)) == [1, 2, 4]

    list_3 = ListNode(val=2, next=ListNode(val=1))
    assert traverse_list(delete_middle(list_3)) == [2]

    list_4 = ListNode(val=1)
    assert traverse_list(delete_middle(list_4)) == []
