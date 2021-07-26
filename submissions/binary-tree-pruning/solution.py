# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_valid(self, node: TreeNode) -> bool:
        if not node:
            return False
        
        if (node.val == 0) and (not self.is_valid(node.left)) and (not self.is_valid(node.right)):
            return False
        else:
            if not self.is_valid(node.left):
                node.left = None
            if not self.is_valid(node.right):
                node.right = None
            return True            

    def pruneTree(self, root: TreeNode) -> TreeNode:      
        if self.is_valid(root):
            return root
        else:
            return None
        
        
