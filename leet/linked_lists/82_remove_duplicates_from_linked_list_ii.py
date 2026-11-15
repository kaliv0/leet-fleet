# 82. Remove Duplicates from Sorted List II
from leet.linked_lists.utils import ListNode, build_list, traverse_list


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
    cases = [
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
        ([], []),
        ([1, 1], []),
    ]

    for inp, result in cases:
        assert (
            actual := traverse_list(delete_duplicates(build_list(inp)))
        ) == result, actual
