# 100. Same Tree
from typing import Optional

from leet.binary_trees.utils import TreeNode


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    return _dfs(p) == _dfs(q)


def _dfs(root):
    if root is None:
        return []

    res = []
    stack = [root]
    while stack:
        if (curr := stack.pop()) is None:
            res.append(curr)
            continue

        res.append(curr.val)
        stack.append(curr.right)
        stack.append(curr.left)
    return res


def is_same_tree_recursive(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True

    # JS flavor
    if (p and p.val) != (q and q.val):
        return False

    return is_same_tree_recursive(p.left, q.left) and is_same_tree_recursive(p.right, q.right)


if __name__ == '__main__':
    p = TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))
    q = TreeNode(val=1, left=TreeNode(2), right=TreeNode(3))
    assert is_same_tree(p, q) is True
    assert is_same_tree_recursive(p, q) is True

    # NB: because of this we need to keep track of all children nodes even if they are None (in iterative dfs approach)
    p = TreeNode(val=1, left=TreeNode(2), right=None)
    q = TreeNode(val=1, left=None, right=TreeNode(2))
    assert is_same_tree(p, q) is False
    assert is_same_tree_recursive(p, q) is False

    p = TreeNode(val=1, left=TreeNode(2), right=TreeNode(1))
    q = TreeNode(val=1, left=TreeNode(1), right=TreeNode(2))
    assert is_same_tree(p, q) is False
    assert is_same_tree_recursive(p, q) is False
