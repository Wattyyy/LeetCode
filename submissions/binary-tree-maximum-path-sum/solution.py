# https://leetcode.com/problems/binary-tree-maximum-path-sum

# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max = -float("inf")

    def calc_sum(self, node):
        if (not node.left) and (not node.right):
            self.max = max(self.max, node.val)
            return node.val

        elif node.left and not node.right:
            left_val = self.calc_sum(node.left)
            res = max(left_val + node.val, node.val)
            self.max = max(self.max, res)
            return res

        elif not node.left and node.right:
            right_val = self.calc_sum(node.right)
            res = max(node.val + right_val, node.val)
            self.max = max(self.max, res)
            return res

        else:
            left_val, right_val = self.calc_sum(node.left), self.calc_sum(node.right)
            res = max(left_val + node.val, node.val, node.val + right_val)
            self.max = max(self.max, res, left_val + node.val + right_val)
            return res

    def maxPathSum(self, root):
        _ = self.calc_sum(root)
        return self.max
