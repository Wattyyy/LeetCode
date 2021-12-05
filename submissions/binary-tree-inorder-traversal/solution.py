# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root):
        self.ans = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            self.ans.append(node.val)
            helper(node.right)

        helper(root)
        return self.ans
