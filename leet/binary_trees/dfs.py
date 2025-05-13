from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs(root):
    if not root:
        return []

    res = []
    stack = deque([root])
    while stack:
        curr = stack.pop()
        res.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res


def dfs_recursive(root):
    if not root:
        return []
    res = []
    _dfs_rec(root, res)
    return res


def _dfs_rec(node, res):
    if node is None:
        return
    res.append(node.val)
    _dfs_rec(node.left, res)
    _dfs_rec(node.right, res)


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

    assert (res := dfs(one)) == [1, 2, 4, 5, 3, 6, 7], res
    assert (res := dfs_recursive(one)) == [1, 2, 4, 5, 3, 6, 7], res

    # case_2
    single = TreeNode(val=1)
    assert dfs(single) == [1]
    assert dfs_recursive(single) == [1]

    # case_3
    assert dfs(None) == []
    assert dfs_recursive(None) == []
