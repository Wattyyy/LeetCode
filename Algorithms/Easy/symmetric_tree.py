# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        def helper(l_node, r_node):
            if (not l_node) and (not r_node):
                return True
            if (not l_node) or (not r_node):
                return False
            return (l_node.val == r_node.val) and helper(l_node.right, r_node.left) and helper(l_node.left, r_node.right)
        
        res = helper(root, root)
        return res
