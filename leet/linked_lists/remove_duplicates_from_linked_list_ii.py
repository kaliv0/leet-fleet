# 82. Remove Duplicates from Sorted List II
from leet.linked_lists.utils import ListNode, traverse_list


def delete_duplicates(head):
    if head is None or head.next is None:
        return head

    dummy = ListNode()
    fast = head
    slow = dummy  # start with dummy node in cases first nodes are duplicates
    slow.next = head

    while fast and fast.next:
        if fast.val == fast.next.val:
            # move beyond duplicates
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            # one more to step outside dups
            fast = fast.next
            # 'attach' first non-duplicate to result list -> skipping dups
            slow.next = fast
        else:
            # only move slow if we are sure there are no dups ahead
            slow = slow.next
            fast = fast.next

    return dummy.next


if __name__ == "__main__":
    list_1 = ListNode(
        val=1, next=ListNode(
            val=2, next=ListNode(
                val=3, next=ListNode(
                    val=3, next=ListNode(
                        val=4, next=ListNode(
                            val=4, next=ListNode(
                                val=5)))))))
    assert traverse_list(delete_duplicates(list_1)) == [1, 2, 5]

    list_2 = ListNode(
        val=1, next=ListNode(
            val=1, next=ListNode(
                val=1, next=ListNode(
                    val=2, next=ListNode(
                        val=3)))))
    assert traverse_list(delete_duplicates(list_2)) == [2, 3]

    assert traverse_list(delete_duplicates(None)) == []
    assert traverse_list(delete_duplicates(ListNode(val=1, next=ListNode(val=1)))) == []
