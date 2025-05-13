from typing import Optional


class ListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    prev = None
    curr = head
    next = curr.next

    while curr.next:
        # reverse
        curr.next = prev
        curr.prev = next
        # move pointers
        prev = curr
        curr = next
        next = curr.next

    curr.next = prev
    curr.prev = None
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


def traverse_back(node: ListNode):
    if not node:
        return []
    res = []
    # go to tail
    while node.next:
        node = node.next
    # move backwards and add values
    while node.prev:
        res.append(node.val)
        node = node.prev
    res.append(node.val)
    return res


if __name__ == "__main__":
    # case_1
    one = ListNode(val=1)  # head
    two = ListNode(val=2, prev=one)
    three = ListNode(val=3, prev=two)
    four = ListNode(val=4, prev=three)
    five = ListNode(val=5, prev=four)  # tail

    one.next = two
    two.next = three
    three.next = four
    four.next = five

    reversed = reverse_list(one)
    assert traverse_list(reversed) == [5, 4, 3, 2, 1]
    assert traverse_back(reversed) == [1, 2, 3, 4, 5]

    # case_2
    one = ListNode(val=1)  # head
    two = ListNode(val=2, prev=one)  # tail
    one.next = two

    reversed = reverse_list(one)
    assert traverse_list(reversed) == [2, 1]
    assert traverse_back(reversed) == [1, 2]

    # case_3
    one = ListNode(val=1)  # head & tail
    assert traverse_list(reverse_list(one)) == [1]

    # case_4
    assert traverse_list(reverse_list(None)) == []
