function sumRootToLeaf(root: TreeNode | null): number {
  let ans = 0;
  function recursion(node: TreeNode, cur: number): void {
    cur += node.val;
    if (node.left === null && node.right === null) {
      ans += cur;
    }
    if (node.left !== null) {
      recursion(node.left, cur << 1);
    }
    if (node.right !== null) {
      recursion(node.right, cur << 1);
    }
    return;
  }
  if (root === null) {
    return 0;
  } else {
    recursion(root, 0);
  }

  return ans;
}


