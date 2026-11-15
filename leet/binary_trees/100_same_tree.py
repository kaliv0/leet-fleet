# 100. Same Tree

from leet.binary_trees.utils import TreeNode


def is_same_tree(p: TreeNode | None, q: TreeNode | None) -> bool:
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


def is_same_tree_recursive(p: TreeNode | None, q: TreeNode | None) -> bool:
    if p is None and q is None:
        return True

    # JS flavor
    if (p and p.val) != (q and q.val):
        return False

    return is_same_tree_recursive(p.left, q.left) and is_same_tree_recursive(
        p.right, q.right
    )  # type:ignore


if __name__ == "__main__":
    # NB: because of this we need to keep track of all children nodes even if they are None (in iterative dfs approach)
    for build, result in (
        (
            lambda: (
                TreeNode(val=1, left=TreeNode(2), right=TreeNode(3)),
                TreeNode(val=1, left=TreeNode(2), right=TreeNode(3)),
            ),
            True,
        ),
        (
            lambda: (
                TreeNode(val=1, left=TreeNode(2), right=None),
                TreeNode(val=1, left=None, right=TreeNode(2)),
            ),
            False,
        ),
        (
            lambda: (
                TreeNode(val=1, left=TreeNode(2), right=TreeNode(1)),
                TreeNode(val=1, left=TreeNode(1), right=TreeNode(2)),
            ),
            False,
        ),
    ):
        p, q = build()
        assert (actual := is_same_tree(p, q)) is result, actual
        assert (actual := is_same_tree_recursive(p, q)) is result, actual
