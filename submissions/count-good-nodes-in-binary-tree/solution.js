/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */


var goodNodes = function(root) {
    var ans = 0;
    const backtrack = function(node, max_val) {
        if (max_val <= node.val) {
            ans += 1;
        }
        if (node.left !== null) {
            if (max_val <= node.left.val) {
                backtrack(node.left, node.left.val);
            }
            else {
                backtrack(node.left, max_val);
            }
        }
        if (node.right !== null) {
            if (max_val <= node.right.val) {
                backtrack(node.right, node.right.val);
            }
            else {
                backtrack(node.right, max_val);
            }
        }
        return
    }
    backtrack(root, root.val)

    return ans;
    
};
