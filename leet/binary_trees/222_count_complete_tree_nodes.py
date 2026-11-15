# 222. Count Complete Tree Nodes

from leet.binary_trees.utils import TreeNode


def count_nodes(root: TreeNode | None) -> int:
    if not root:
        return 0

    left_depth = _get_depth(root.left)
    right_depth = _get_depth(root.right)
    if left_depth == right_depth:
        return 2**left_depth + count_nodes(root.right)
    return 2**right_depth + count_nodes(root.left)


def _get_depth(node):
    if not node:
        return 0
    return 1 + _get_depth(node.left)


#######################
def count_nodes_alt(root: TreeNode | None) -> int:
    if not root:
        return 0

    left = right = root
    left_depth = 0
    while left:
        left_depth += 1
        left = left.left

    right_depth = 0
    while right:
        right_depth += 1
        right = right.right

    if left_depth == right_depth:
        return (
            2**left_depth - 1
        )  # standard depth if tree is perfect (root is at height one)
    return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == "__main__":
    for build, result in (
        (
            lambda: TreeNode(
                1,
                left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)),
                right=TreeNode(3, left=TreeNode(6)),
            ),
            6,
        ),
        (lambda: None, 0),
        (lambda: TreeNode(1), 1),
    ):
        root = build()
        assert (actual := count_nodes(root)) == result, actual
        assert (actual := count_nodes_alt(root)) == result, actual
