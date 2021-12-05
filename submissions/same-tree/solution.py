# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True
        
    def search(self, p_node, q_node):
        if (not p_node and not q_node) or (not self.ans):
            return
        
        if not p_node or not q_node:
            self.ans = False
            return
        
        if p_node.val == q_node.val:
            self.search(p_node.left, q_node.left)
            self.search(p_node.right, q_node.right)
            
        else:
            self.ans = False
            return
            
    def isSameTree(self, p, q):
        self.search(p, q)
        return self.ans
        
        
        
        