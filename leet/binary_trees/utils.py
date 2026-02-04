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


def dfs(root):
    if not root:
        return []

    res = []
    stack = [root]
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
    res.append(node.val)
    if node.left:
        _dfs_rec(node.left, res)
    if node.right:
        _dfs_rec(node.right, res)
