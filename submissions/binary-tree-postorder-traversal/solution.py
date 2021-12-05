# https://leetcode.com/problems/binary-tree-postorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        self.ans = []
        def helper(node):
            if not node:
                return 
            helper(node.left)
            helper(node.right)
            self.ans.append(node.val)
        helper(root)
        return self.ans
            
            