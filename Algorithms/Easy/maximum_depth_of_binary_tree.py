# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        def helper(node, cnt):
            if not node:
                return cnt
            else:
                return max(helper(node.left, cnt+1), helper(node.right, cnt+1))
        
        cnt = 0
        return helper(root, cnt)
