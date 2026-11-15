# 328. Odd Even Linked List

from leet.linked_lists.utils import ListNode, build_list, traverse_list


def odd_even_dance(head):
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    new_head = even

    while even and even.next:
        # skip/ remove node, go to next location
        odd.next = odd.next.next
        odd = odd.next
        # same choreography
        even.next = even.next.next
        even = even.next
    # attach both lists
    odd.next = new_head
    return head


def odd_even_list(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head

    curr = head

    even = ListNode()
    other = even
    while curr.next and curr.next.next:
        # detach even node from main list
        tmp = curr.next
        # attach prev to next odd
        curr.next = curr.next.next
        # attach even to new list
        other.next = tmp
        # move pointers
        curr = curr.next
        other = other.next

    # detach last one
    tmp = curr.next
    other.next = tmp
    # combine both lists
    curr.next = even.next

    return head


if __name__ == "__main__":
    cases = [
        ([1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 4, 6]),
        ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4]),
        ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
        ([1, 2], [1, 2]),
        ([1], [1]),
        ([], []),
    ]

    for inp, result in cases:
        assert (actual := traverse_list(odd_even_dance(build_list(inp)))) == result, (
            actual
        )
