# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            tmp_queue = []
            tmp_vals = []
            for node in queue:
                tmp_vals.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            ans.append(tmp_vals)
            queue = tmp_queue
        return ans
            
        
