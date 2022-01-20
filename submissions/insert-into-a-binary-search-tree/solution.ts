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

function insertIntoBST(root: TreeNode | null, val: number): TreeNode | null {
    if (root === null) {
        let res: TreeNode = new TreeNode(val);
        return res;
    }
    function insertNode(prev: TreeNode, pos: TreeNode | null, isLeft: boolean, val: number): void {
        if (pos === null) {
            if (isLeft) {
                prev.left = new TreeNode(val);
            }
            else {
                prev.right = new TreeNode(val);
            }
        }
        else {
            if (val < pos.val) {
                insertNode(pos, pos.left, true, val);
            }
            else {
                insertNode(pos, pos.right, false, val);
            }
        }
    }

    if (val < root.val) {
        insertNode(root, root.left, true, val);
    }
    else {
        insertNode(root, root.right, false, val);
    }
    return root;
};
