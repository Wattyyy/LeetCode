# https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        if not root:
            return False
        self.bool = False

        def helper(node, cnt, sum):
            if not node:
                return
            cnt += node.val
            if cnt == sum and not node.left and not node.right:
                self.bool = True
                return
            else:
                helper(node.left, cnt, sum)
                helper(node.right, cnt, sum)

        helper(root, 0, sum)
        return self.bool
