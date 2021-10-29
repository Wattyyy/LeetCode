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

function pathSum(root: TreeNode | null, targetSum: number): number {
    let ans = 0;
    
    function check_sum(node: TreeNode, current_sum: number, target: number): void {
        let val = current_sum + node.val;
        if (val === target) {
            ans += 1;
        }
        if (node.left !== null) {
            check_sum(node.left, val, target);
        }
        if (node.right !== null) {
            check_sum(node.right, val, target);
        }
        return;
    }

    function dfs(node: TreeNode, target: number): void {
        check_sum(node, 0, target);
        if (node.left !== null) {
            dfs(node.left, target);
        }
        if (node.right !== null) {
            dfs(node.right, target);
        }
        return;
    }
    if (root === null) {
        return 0;
    }
    else {
        dfs(root, targetSum);
        return ans;
    }

};


