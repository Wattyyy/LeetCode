# https://leetcode.com/problems/path-sum-ii

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = []

    def backtrack(self, node, sum, val, ls):
        if not node.left and not node.right:
            if val == sum:
                self.ans.append(ls[:])
        if node.left:
            val += node.left.val
            ls.append(node.left.val)
            self.backtrack(node.left, sum, val, ls)
            val -= node.left.val
            ls.pop()
        if node.right:
            val += node.right.val
            ls.append(node.right.val)
            self.backtrack(node.right, sum, val, ls)
            val -= node.right.val
            ls.pop()

    def pathSum(self, root, sum):
        if not root:
            return self.ans
        self.backtrack(root, sum, root.val, [root.val])
        return self.ans
