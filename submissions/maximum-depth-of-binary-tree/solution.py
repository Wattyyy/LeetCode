# https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        self.ans = 0
        def helper(node, height):
            if not node.left and not node.right:
                self.ans = max(height, self.ans)
            if node.left:
                helper(node.left, height+1)
            if node.right:
                helper(node.right, height+1)
        helper(root, 1)
        return self.ans
        
            
        