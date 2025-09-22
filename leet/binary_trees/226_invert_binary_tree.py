# 226. Invert Binary Tree

from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def reverse_tree(root):
    queue = deque([root])
    while queue:
        curr = queue.pop()
        curr.left, curr.right = curr.right, curr.left
        if curr.left:
            queue.appendleft(curr.left)
        if curr.right:
            queue.appendleft(curr.right)
    return root


# traverse tree to validate result
def bfs(root):
    if not root:
        return []
    res = []
    queue = deque([root])
    while queue:
        curr = queue.pop()
        res.append(curr.val)
        if curr.left:
            queue.appendleft(curr.left)
        if curr.right:
            queue.appendleft(curr.right)
    return res


if __name__ == "__main__":
    #         1
    #   2         3
    # 4    5    6   7

    # inverted
    #        1
    #   3         2
    # 7   6    5    4

    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)

    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven

    assert (res := bfs(reverse_tree(one))) == [1, 3, 2, 7, 6, 5, 4], res

    # case_2
    single = TreeNode(val=1)
    assert bfs(single) == [1]

    # case_3
    assert bfs(None) == []
