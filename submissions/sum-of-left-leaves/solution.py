# https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        
    def sumup(self, node, state):
        if (not node.left) and (not node.right) and (state == 'left'):
            self.ans += node.val
            return
        if node.left:
            self.sumup(node.left, 'left')
        if node.right:
            self.sumup(node.right, 'right')

    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        self.sumup(root, 'right')
        return self.ans
        
    
        