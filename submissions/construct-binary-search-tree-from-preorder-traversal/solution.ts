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

function bstFromPreorder(preorder: number[]): TreeNode | null {
    let end = new TreeNode(100000001)
    let root = new TreeNode(preorder[0]);
    let node_stack: Array<TreeNode> = [end, root];
    let number_stack: Array<number> = [100000001, preorder[0]];
    
    for (let i = 1; i < preorder.length; i++) {
        let num = preorder[i];
        let node = new TreeNode(preorder[i]);
        if (number_stack[number_stack.length - 1] > num) {
            node_stack[node_stack.length - 1].left = node;
            node_stack.push(node);
            number_stack.push(num);
        }
        else {
            while (number_stack[number_stack.length - 1] < num) {
                var prev_node = node_stack.pop();
                number_stack.pop();
            }
            if (prev_node !== undefined) {
                prev_node.right = node;
                node_stack.push(node);
                number_stack.push(num);
            }
        }
    }
    return root;
};


