# https://leetcode.com/problems/minimum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        ans = set()
        def helper(node, depth):
            if (not node.left) and (not node.right):
                ans.add(depth)
                return 
            if node.right:
                helper(node.right, depth+1)
            if node.left:
                helper(node.left, depth+1)
        helper(root, 1)
        return min(ans)
        
        
