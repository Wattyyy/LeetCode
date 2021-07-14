// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root):
        self.ans = [0] * 10001
        self.ans[0] = -float('inf')
        def traverse(node, level):
            self.ans[level] += node.val
            if not node.left and not node.right:
                return
            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)
        traverse(root, 1)
        tmp = [0, self.ans[0]]
        for i, val in enumerate(self.ans):
            if tmp[1] < val:
                tmp = [i, val]
        return tmp[0]


        
            
        