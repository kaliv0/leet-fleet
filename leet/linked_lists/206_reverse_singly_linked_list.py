# 206. Reverse Linked List

from leet.linked_lists.utils import ListNode, build_list, traverse_list


def reverse_list(head: ListNode | None) -> ListNode | None:
    if not head or not head.next:
        return head

    prev = None
    curr = head
    while curr.next:
        # reverse
        temp = curr.next
        curr.next = prev
        # move pointers
        prev = curr
        curr = temp
    # adjust tail and return as new head
    curr.next = prev
    return curr


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([1], [1]),
        ([], []),
    ]

    for inp, result in cases:
        assert (actual := traverse_list(reverse_list(build_list(inp)))) == result, (
            actual
        )
