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

function isCousins(root: TreeNode | null, x: number, y: number): boolean {
    let queue: Array<TreeNode> = [root];
    while (0 < queue.length) {
        let new_queue: Array<TreeNode> = [];
        let cnt = 0;
        for (let i = 0; i < queue.length; i++) {
            let node = queue[i];
            let tmp: Array<number> = [];
            if (node.left !== null) {
                new_queue.push(node.left);
                tmp.push(node.left.val);
                if (node.left.val === x || node.left.val === y) {
                    cnt += 1;
                }
            }
            if (node.right !== null) {
                new_queue.push(node.right);
                tmp.push(node.right.val);
                if (node.right.val === x || node.right.val === y) {
                    cnt += 1;
                }
            }
            if (tmp.includes(x) && tmp.includes(y)) {
                return false;
            }
        }

        if (2 === cnt) {
            return true;
        }
        queue = new_queue;
    }

    return false;
};
