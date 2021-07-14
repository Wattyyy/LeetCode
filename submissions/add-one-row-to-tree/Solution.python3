// https://leetcode.com/problems/add-one-row-to-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_node = TreeNode(v)
            new_node.left = root
            return new_node
            
        # BFS
        roots = [root]
        cur_depth = 2
        while cur_depth < d:
            next_roots = []
            for node in roots:
                if node.left:
                    next_roots.append(node.left)
                if node.right:
                    next_roots.append(node.right)
            cur_depth += 1
            roots = next_roots
        
        
        for node in roots:
            # left
            new_node = TreeNode(v)
            if node.left:
                new_node.left = node.left
            node.left = new_node
            
            # right
            new_node = TreeNode(v)
            if node.right:
                new_node.right = node.right
            node.right = new_node
        
        return root
            
