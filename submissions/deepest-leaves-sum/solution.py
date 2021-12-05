# https://leetcode.com/problems/deepest-leaves-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque


class Solution:
    def deepestLeavesSum(self, root):
        d = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            d[depth].append(node.val)
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        max_depth = max(d.keys())
        return sum(d[max_depth])
