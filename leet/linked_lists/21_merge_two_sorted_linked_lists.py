# 21. Merge Two Sorted Lists

from leet.linked_lists.utils import traverse_list, ListNode, build_list


def merge_two_lists(
    list_1: ListNode | None, list_2: ListNode | None
) -> ListNode | None:
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
    cases = [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([0], [], [0]),
        ([2], [1, 3, 4], [1, 2, 3, 4]),
        ([5], [1, 2, 4], [1, 2, 4, 5]),
    ]

    for a, b, result in cases:
        assert (
            actual := traverse_list(merge_two_lists(build_list(a), build_list(b)))
        ) == result, actual
