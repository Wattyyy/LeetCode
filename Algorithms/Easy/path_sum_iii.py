# https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = 0

    def traverse(self, node, val, sum):
        if val == sum:
            self.ans += 1
        if not node.left and not node.right:
            return
        if node.left:
            val += node.left.val
            self.traverse(node.left, val, sum)
            val -= node.left.val
        if node.right:
            val += node.right.val
            self.traverse(node.right, val, sum)
            val -= node.right.val

    def dfs(self, node, sum):
        if not node:
            return
        self.traverse(node, node.val, sum)
        self.dfs(node.left, sum)
        self.dfs(node.right, sum)
        
    def pathSum(self, root, sum):
        self.dfs(root, sum)
        return self.ans
        
