# https://leetcode.com/problems/closest-binary-search-tree-value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.distance = []

    def traverse(self, node, target):
        self.distance.append([abs(node.val - target), node.val])
        if node.left:
            self.traverse(node.left, target)
        if node.right:
            self.traverse(node.right, target)

    def closestValue(self, root, target):
        self.traverse(root, target)
        self.distance = sorted(self.distance)
        return self.distance[0][1]
