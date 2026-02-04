from collections import deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    assert (res := bfs(one)) == [1, 2, 3, 4, 5, 6, 7], res

    # case_2
    single = TreeNode(val=1)
    assert bfs(single) == [1]

    # case_3
    assert bfs(None) == []
