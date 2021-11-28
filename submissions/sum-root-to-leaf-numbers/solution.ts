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

function sumNumbers(root: TreeNode | null): number {
  if (root === null) {
    return 0;
  }
  let ans = 0;
  let queue: Array<[TreeNode, number]> = [[root, root.val]];
  while (0 < queue.length) {
    const [node, val] = queue.shift()!;
    if (node.left === null && node.right === null) {
      ans += val;
    } else {
      if (node.left !== null) {
        queue.push([node.left, val * 10 + node.left.val]);
      }
      if (node.right !== null) {
        queue.push([node.right, val * 10 + node.right.val]);
      }
    }
  }

  return ans;
}


