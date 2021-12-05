# https://leetcode.com/problems/validate-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        self.bool = True
        def helper(node, l_lim, u_lim):
            if not node:
                return 
            if (l_lim < node.val) and (node.val < u_lim):
                helper(node.left, l_lim, node.val)
                helper(node.right, node.val, u_lim)
            else:
                self.bool = False
                return 
            
        helper(root, -float("inf"), float("inf"))
        return self.bool