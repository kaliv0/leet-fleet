# 19. Remove Nth Node From End of List

from leet.linked_lists.utils import ListNode, build_list, traverse_list


def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:
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
    for inp, n, result in (
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 2, [2]),
    ):
        assert (
            actual := traverse_list(remove_nth_from_end(build_list(inp), n))
        ) == result, actual
