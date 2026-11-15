# 138. Copy List with Random Pointer


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
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


def copy_random_list(head: Node | None) -> Node | None:
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

    def build(desc):
        if not desc:
            return None
        nodes = [Node(v) for v, _ in desc]
        for i, (_, r) in enumerate(desc):
            if i + 1 < len(nodes):
                nodes[i].next = nodes[i + 1]
            nodes[i].random = None if r is None else nodes[r]
        return nodes[0]

    for inp, result in (
        (
            [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
            [[7, None], [13, 7], [11, 1], [10, 11], [1, 7]],
        ),
    ):
        assert (actual := traverse_list(copy_random_list(build(inp)))) == result, actual
