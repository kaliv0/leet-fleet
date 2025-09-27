// 112. Path Sum
class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

// traverse tree via dfs, reduce target with current val on each level,
// when reaching a leaf if reduced target equals node value -> we've found a valid 'sum path'
function hasPathSum(root: TreeNode | null, targetSum: number): boolean {
    if (root === null) {
        return false;
    }

    // base case -> we've reached the leaf level
    if (root.left === null && root.right === null) {
        return targetSum === root.val;
    }

    targetSum -= root.val;
    return hasPathSum(root.left, targetSum) || hasPathSum(root.right, targetSum);
}
