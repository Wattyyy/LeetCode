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

function maxDepth(root: TreeNode | null): number {
  let ans = 0;
  function dfs(node: TreeNode | null, cnt: number): void {
    if (node === null) {
      ans = Math.max(ans, cnt);
    } else {
      dfs(node.left, cnt + 1);
      dfs(node.right, cnt + 1);
    }
  }
  dfs(root, 0);
  return ans;
}


