# 61. Rotate List

from leet.linked_lists.utils import ListNode, build_list, traverse_list


def rotate_right(head: ListNode | None, k: int) -> ListNode | None:
    if head is None or head.next is None or k == 0:
        return head

    # find list length
    curr = head
    list_len = 1
    while curr and curr.next:
        curr = curr.next
        list_len += 1
    # readjust k
    k = k % list_len
    if k == 0:
        return head

    dummy = ListNode()
    dummy.next = head
    fast = head
    slow = dummy
    counter = 1
    # find point to break list in two
    while fast.next:
        fast = fast.next
        counter += 1
        if counter > k:
            slow = slow.next
    # detach sib-list
    new_head = slow.next
    slow.next = None
    # append in front
    second = dummy.next
    dummy.next = new_head
    # find last node of new_head to attach to second sub_list
    while new_head and new_head.next:
        new_head = new_head.next
    new_head.next = second

    return dummy.next


def rotate_right_brute_force(head: ListNode | None, k: int) -> ListNode | None:
    if head is None or head.next is None:
        return head

    dummy = ListNode()
    dummy.next = head

    for _ in range(k):
        # find tail
        curr = dummy.next
        while curr.next.next:
            curr = curr.next
        # rotate -> detach tail, insert between dummy and head
        tmp = curr.next
        curr.next = None
        second = dummy.next
        dummy.next = tmp
        tmp.next = second

    return dummy.next


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
        ([1, 2], 1, [2, 1]),
        ([1, 2], 2, [1, 2]),
        ([], 2, []),
        ([1], 4, [1]),
        ([1], 0, [1]),
    ]

    for inp, k, result in cases:
        assert (actual := traverse_list(rotate_right(build_list(inp), k))) == result, (
            actual
        )
