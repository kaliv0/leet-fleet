# 21. Merge Two Sorted Lists

from typing import Optional

from leet.linked_lists.utils import traverse_list, ListNode


def merge_two_lists(list_1: Optional[ListNode], list_2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    while list_1 and list_2:
        if list_1.val < list_2.val:
            curr.next = list_1
            curr = curr.next
            list_1 = list_1.next
        else:
            curr.next = list_2
            curr = curr.next
            list_2 = list_2.next

    if list_1:
        curr.next = list_1
    elif list_2:
        curr.next = list_2

    return dummy.next


if __name__ == "__main__":
    # case_1 -> first_list = [1, 2, 4], second_list = [1, 3, 4], res = [1,1,2,3,4,4]
    list_1 = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=4
            )
        )
    )
    list_2 = ListNode(
        val=1,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4
            )
        )
    )
    assert traverse_list(merge_two_lists(list_1, list_2)) == [1, 1, 2, 3, 4, 4]

    # case_2 -> first_list = [], second_list = [], res = []
    list_1 = None
    list_2 = None
    assert traverse_list(merge_two_lists(list_1, list_2)) == []

    # case_3 -> first_list = [0], second_list = [], res = []
    list_1 = ListNode(val=0)
    list_2 = None
    assert traverse_list(merge_two_lists(list_1, list_2)) == [0]

    # case_4 -> first_list = [2], second_list = [1, 3, 4], res = [1,2,3,4]
    list_1 = ListNode(val=2)
    list_2 = ListNode(
        val=1,
        next=ListNode(
            val=3,
            next=ListNode(
                val=4
            )
        )
    )
    assert traverse_list(merge_two_lists(list_1, list_2)) == [1, 2, 3, 4]

    # case_5 -> first_list = [5], second_list = [1, 2, 4], res = [1,2,4,5]
    list_1 = ListNode(val=5)
    list_2 = ListNode(
        val=1,
        next=ListNode(
            val=2,
            next=ListNode(
                val=4
            )
        )
    )
    assert traverse_list(merge_two_lists(list_1, list_2)) == [1, 2, 4, 5]
