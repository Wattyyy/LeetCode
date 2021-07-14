// https://leetcode.com/problems/maximum-width-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        ans = 1
        queue = deque([(root, 0)])
        while queue:
            min_val, max_val = float('inf'), -float('inf')
            nx = deque([])
            for node, index in queue:
                if node.left:
                    new_idx = index + index
                    min_val = min(min_val, new_idx)
                    max_val = max(max_val, new_idx)
                    nx.append((node.left, new_idx))
                if node.right:
                    new_idx = index + index + 1
                    min_val = min(min_val, new_idx)
                    max_val = max(max_val, new_idx)
                    nx.append((node.right, new_idx))
            ans = max(ans, max_val - min_val + 1)
            queue = nx
        return ans
        
        
        
        