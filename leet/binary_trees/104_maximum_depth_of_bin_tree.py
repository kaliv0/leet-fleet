# 104. Maximum Depth of Binary Tree

from collections import deque
from typing import Optional

from leet.binary_trees.utils import TreeNode, bfs


def max_depth(root):
    if not root:
        return 0

    maximum_depth = 0
    stack = deque([(root, 1)])
    while stack:
        curr_node, curr_depth = stack.pop()
        if curr_node.left:
            stack.append((curr_node.left, curr_depth + 1))
        if curr_node.right:
            stack.append((curr_node.right, curr_depth + 1))
        if not curr_node.left and not curr_node.right:
            # if there are no children we've reached leaf-level
            maximum_depth = max(maximum_depth, curr_depth)

    return maximum_depth


def max_depth_rec(node: Optional[TreeNode]) -> int:
    if not node:
        return 0
    left_depth = max_depth_rec(node.left)
    right_depth = max_depth_rec(node.right)
    return max(left_depth, right_depth) + 1
    # NB: add 1 to account for current level


if __name__ == "__main__":
    #        3
    #   9         20
    #         15    17

    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seventeen = TreeNode(17)

    three.left = nine
    three.right = twenty
    twenty.left = fifteen
    twenty.right = seventeen

    assert (res := bfs(three)) == [3, 9, 20, 15, 17], res
    assert (res := max_depth(three)) == 3, res
    assert (res := max_depth_rec(three)) == 3, res

    # case_2

    #        1
    #   2        3
    # 4    5

    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    one.left = two
    one.right = three
    two.left = four
    two.right = five

    assert (res := bfs(one)) == [1, 2, 3, 4, 5], res
    assert (res := max_depth(one)) == 3, res
    assert (res := max_depth_rec(one)) == 3, res

    # case_3

    #        1
    #   2        3
    # 4             5

    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)

    one.left = two
    one.right = three
    two.left = four
    three.right = five

    assert (res := bfs(one)) == [1, 2, 3, 4, 5], res
    assert (res := max_depth(one)) == 3, res
    assert (res := max_depth_rec(one)) == 3, res

    # case_3
    root = TreeNode(val=1)
    leaf = TreeNode(val=2)
    root.right = leaf
    assert bfs(root) == [1, 2]
    assert (res := max_depth(root)) == 2, res
    assert (res := max_depth_rec(root)) == 2, res

    # case_4
    single = TreeNode(val=1)
    assert (res := max_depth(single)) == 1, res
    assert (res := max_depth_rec(single)) == 1, res

    # case_5
    assert bfs(None) == []
    assert (res := max_depth(None)) == 0, res
    assert (res := max_depth_rec(None)) == 0, res
