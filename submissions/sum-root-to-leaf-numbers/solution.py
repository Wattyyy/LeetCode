// https://leetcode.com/problems/sum-root-to-leaf-numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def traverse(self, node, val):
        val = val * 10 + node.val
        if not node.left and not node.right:
            self.ans += val
        if node.left:
            self.traverse(node.left, val)
        if node.right:
            self.traverse(node.right, val)
        
    def sumNumbers(self, root):
        if not root:
            return 0
        self.traverse(root, 0)
        return self.ans

        
        