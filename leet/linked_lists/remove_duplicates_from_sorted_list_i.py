# 83. Remove Duplicates from Sorted List

from leet.linked_lists.utils import ListNode, traverse_list


def delete_duplicates(head):
    if head is None or head.next is None:
        return head

    curr = head
    while curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


if __name__ == "__main__":
    list_1 = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2)))
    assert traverse_list(delete_duplicates(list_1)) == [1, 2]

    list_2 = ListNode(
        val=1, next=ListNode(
            val=1, next=ListNode(
                val=2, next=ListNode(
                    val=3, next=ListNode(
                        val=3)))))
    assert traverse_list(delete_duplicates(list_2)) == [1, 2, 3]

    list_3 = ListNode(val=1, next=ListNode(val=1))
    assert traverse_list(delete_duplicates(list_3)) == [1]

    list_4 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3)))
    assert traverse_list(delete_duplicates(list_4)) == [1, 2, 3]

    list_5 = None
    assert traverse_list(delete_duplicates(list_5)) == []
