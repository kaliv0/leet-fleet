# 83. Remove Duplicates from Sorted List

from leet.linked_lists.utils import ListNode, build_list, traverse_list


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
    cases = [
        ([1, 1, 2], [1, 2]),
        ([1, 1, 2, 3, 3], [1, 2, 3]),
        ([1, 1], [1]),
        ([1, 2, 3], [1, 2, 3]),
        ([], []),
    ]

    for inp, result in cases:
        assert (
            actual := traverse_list(delete_duplicates(build_list(inp)))
        ) == result, actual
