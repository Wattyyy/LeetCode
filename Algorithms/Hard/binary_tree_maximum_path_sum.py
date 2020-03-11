# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        if not root:
            return 0
        self.ans = -float('inf')
        def dp(node):
            if node.left and node.right:
                l_val, r_val = dp(node.left), dp(node.right)
                self.ans = max(self.ans, l_val + r_val + node.val, l_val + node.val, r_val + node.val, node.val)
                res = max(l_val + node.val, r_val + node.val, node.val)
            elif node.left and not node.right:
                l_val = dp(node.left)
                self.ans = max(self.ans, l_val + node.val, node.val)
                res = max(l_val + node.val, node.val)
            elif not node.left and node.right:
                r_val = dp(node.right)
                self.ans = max(self.ans, r_val + node.val, node.val)
                res = max(r_val + node.val, node.val)
            else:
                self.ans = max(self.ans, node.val)
                res = node.val
            return res
        
        dp(root)
        return self.ans
        
            
        
        