# 138. Copy List with Random Pointer
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def traverse_list(node: Node):
    if not node:
        return []

    res = []
    while node.next:
        res.append([node.val, node.random and node.random.val])
        node = node.next
    res.append([node.val, node.random and node.random.val])
    return res


def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    if head is None:
        return None

    dummy = Node(0)
    curr = dummy
    pointer = head
    random_map = {}
    while pointer:
        new_node = Node(x=pointer.val, random=pointer.random)
        curr.next = new_node
        random_map[pointer] = new_node

        curr = curr.next
        pointer = pointer.next

    curr = dummy.next
    while curr:
        curr.random = random_map.get(curr.random)
        curr = curr.next

    return dummy.next


if __name__ == "__main__":
    # case_1 -> [[7,null],[13,0],[11,4],[10,2],[1,0]]
    head = Node(7)
    node_1 = Node(13)
    node_2 = Node(11)
    node_3 = Node(10)
    node_4 = Node(1)

    head.next = node_1
    head.random = None

    node_1.next = node_2
    node_1.random = head

    node_2.next = node_3
    node_2.random = node_4

    node_3.next = node_4
    node_3.random = node_2

    node_4.next = None
    node_4.random = head

    assert traverse_list(copy_random_list(head)) == [[7, None], [13, 7], [11, 1], [10, 11], [1, 7]]
