/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function sumOfLeftLeaves(root: TreeNode | null): number {
    if (root === null) {
        return 0;
    }
    let queue: Array<[TreeNode, boolean]> = [[root, false]];
    let ans = 0;
    while (0 < queue.length) {
        const [node, isLeft] = queue.shift()!;
        if (node.left === null && node.right === null && isLeft) {
            ans += node.val;
        }
        if (node.left) {
            queue.push([node.left, true]);
        }
        if (node.right) {
            queue.push([node.right, false]);
        }
    }

    return ans;
};
