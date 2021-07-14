// https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.nums = list()

    def traverse(self, node):
        self.nums.append(node.val)
        if node.left:
            self.traverse(node.left)
        if node.right:
            self.traverse(node.right)

    def kthSmallest(self, root, k):
        if not root:
            return 0
        self.traverse(root)
        self.nums = sorted(self.nums)
        return self.nums[k-1]
        