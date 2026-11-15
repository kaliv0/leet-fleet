# 86. Partition List
from leet.linked_lists.utils import ListNode, build_list, traverse_list


def partition(head, x):
    if head is None or head.next is None:
        return head
    # create two new lists
    lesser = ListNode()
    l_pointer = lesser

    bigger = ListNode()
    b_pointer = bigger

    curr = head
    while curr:
        if curr.val >= x:
            # attach to bigger list
            b_pointer.next = curr
            b_pointer = curr
        else:
            l_pointer.next = curr
            l_pointer = curr
        # move  to next node
        curr = curr.next
    # terminate bigger list to avoid circular reference
    if b_pointer.next:
        b_pointer.next = None
    # combine lists
    l_pointer.next = bigger.next
    return lesser.next


if __name__ == "__main__":
    for inp, x, result in (([1, 4, 3, 2, 5, 2], 3, [1, 2, 2, 4, 3, 5]),):
        assert (actual := traverse_list(partition(build_list(inp), x))) == result, (
            actual
        )
