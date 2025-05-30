from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
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


def traverse_list(node: ListNode):
    if not node:
        return []

    res = []
    while node.next:
        res.append(node.val)
        node = node.next
    res.append(node.val)
    return res


if __name__ == "__main__":
    # case_1
    five = ListNode(val=5, next=None)  # tail
    four = ListNode(val=4, next=five)
    three = ListNode(val=3, next=four)
    two = ListNode(val=2, next=three)
    one = ListNode(val=1, next=two)  # head

    assert traverse_list(reverse_list(one)) == [5, 4, 3, 2, 1]

    # case_2
    two = ListNode(val=2, next=None)  # tail
    one = ListNode(val=1, next=two)  # head
    assert traverse_list(reverse_list(one)) == [2, 1]

    # case_3
    one = ListNode(val=1, next=None)  # head & tail
    assert traverse_list(reverse_list(one)) == [1]

    # case_4
    assert traverse_list(res := reverse_list(None)) == []
