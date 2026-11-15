# 101. Symmetric Tree

from leet.binary_trees.utils import TreeNode


def is_symmetric(root: TreeNode | None) -> bool:
    if not (root.left or root.right):
        return True

    # visit left subtree
    l_res = []
    stack = [root.left]
    while stack:
        if (curr := stack.pop()) is None:
            l_res.append(curr)
            continue

        l_res.append(curr.val)
        stack.append(curr.left)
        stack.append(curr.right)

    # visit right subtree
    r_res = []
    stack = [root.right]
    while stack:
        if (curr := stack.pop()) is None:
            r_res.append(curr)
            continue

        r_res.append(curr.val)
        stack.append(curr.right)
        stack.append(curr.left)

    return l_res == r_res


#########################
def is_symmetric_recursive(root: TreeNode | None) -> bool:
    return _is_mirror(root.left, root.right)


def _is_mirror(left, right):
    if not left and not right:
        return True

    if not left or not right:
        return False

    return (
        (left.val == right.val)
        and (_is_mirror(left.left, right.right))
        and (_is_mirror(left.right, right.left))
    )


if __name__ == "__main__":
    for build, result in (
        (
            lambda: TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
                right=TreeNode(2, left=TreeNode(4), right=TreeNode(3)),
            ),
            True,
        ),
        (
            lambda: TreeNode(
                1,
                left=TreeNode(2, right=TreeNode(3)),
                right=TreeNode(2, right=TreeNode(3)),
            ),
            False,
        ),
        (lambda: TreeNode(1), True),
    ):
        root = build()
        assert (actual := is_symmetric(root)) is result, actual
        assert (actual := is_symmetric_recursive(root)) is result, actual
