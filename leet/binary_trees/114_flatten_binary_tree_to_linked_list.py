# 114. Flatten Binary Tree to Linked List
from typing import Optional

from leet.binary_trees.utils import TreeNode


def flatten_naive(root: Optional[TreeNode]) -> None:
    # Do not return anything, modify root in-place instead.
    if not root:
        return

    res = []
    stack = [root]
    while stack:
        if curr := stack.pop():
            res.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)

    # for val in res[:-1]:
    for val in res:
        root.val = val
        root.left = None
        root.right = TreeNode(None)
        root = root.right

    # root.val = res[-1]


#######################
def flatten(root: Optional[TreeNode]) -> None:
    # Morris' traversal
    if not root:
        return

    node = root
    while node:
        if node.left:
            # find right most leaf in left subtree
            prev = node.left
            while prev.right:
                prev = prev.right
            # attach right subtree to it
            prev.right = node.right

            # switch subtrees -> move left one to be right (original right already attached)
            node.right = node.left
            node.left = None
        # by switching subtrees and move one level lower on right side
        # we are progressively flattening the tree to have only children on the right side
        node = node.right


if __name__ == '__main__':

    def _traverse(root):
        res = []
        while root and root.val is not None:
            res.append(str(root.val))
            root = root.right

        return ' -> '.join(res)


    root = TreeNode(1,
                    left=TreeNode(2,
                                  left=TreeNode(3),
                                  right=TreeNode(4)),
                    right=TreeNode(5,
                                   left=None,
                                   right=TreeNode(6)))

    flatten(root)
    assert _traverse(root) == '1 -> 2 -> 3 -> 4 -> 5 -> 6'

    root = None
    flatten(root)
    assert _traverse(root) == ''

    root = TreeNode(0)
    flatten(root)
    assert _traverse(root) == '0'
