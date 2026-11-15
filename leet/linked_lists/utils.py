# @skip: helper
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class DoublyListNode(ListNode):
    def __init__(self, val=0, prev=None, next=None):
        super().__init__(val, next)
        self.prev = prev


def build_list(vals: list) -> ListNode | None:
    if not vals:
        return None
    head = curr = ListNode(vals[0])
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def traverse_list(node: ListNode):
    if not node:
        return []

    res = []
    while node.next:
        res.append(node.val)
        node = node.next
    res.append(node.val)
    return res


def traverse_back(node: DoublyListNode):
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
