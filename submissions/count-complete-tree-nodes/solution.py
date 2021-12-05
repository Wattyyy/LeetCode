# https://leetcode.com/problems/count-complete-tree-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
        
    def count(self, node):
        self.ans += 1
        if node.left:
            self.count(node.left)
        if node.right:
            self.count(node.right)
            
    def countNodes(self, root):
        if not root:
            return 0
        self.count(root)
        return self.ans
        
        
        