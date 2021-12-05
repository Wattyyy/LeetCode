# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def backtrack(self, node) -> None:
        """
        convert node value into sum
        """
        if not node.left and not node.right:
            return
        if node.left:
            self.backtrack(node.left)
            node.val += node.left.val
        if node.right:
            self.backtrack(node.right)
            node.val += node.right.val
        return

    def solve(self, root, node) -> None:
        self.ans = max((root.val - node.val) * node.val, self.ans)
        if node.left:
            self.solve(root, node.left)
        if node.right:
            self.solve(root, node.right)
        return

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.backtrack(root)
        if root.left:
            self.solve(root, root.left)
        if root.right:
            self.solve(root, root.right)
        return self.ans % (10 ** 9 + 7)
