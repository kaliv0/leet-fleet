# 226. Invert Binary Tree

from collections import deque

from leet.binary_trees.utils import TreeNode, bfs


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


if __name__ == "__main__":

    def _build_full():
        #         1
        #   2         3
        # 4    5    6   7
        #
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
        return one

    for kind, build, result in (
        ("invert", _build_full, [1, 3, 2, 7, 6, 5, 4]),
        ("bfs", lambda: TreeNode(val=1), [1]),
        ("bfs", lambda: None, []),
    ):
        root = build()
        if kind == "invert":
            assert (actual := bfs(reverse_tree(root))) == result, actual
        else:
            assert (actual := bfs(root)) == result, actual
