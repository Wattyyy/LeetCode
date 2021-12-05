# https://leetcode.com/problems/average-of-levels-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        output = []
        if not root:
            return output
        nodes = [root]
        while 0 < len(nodes):
            node_vals = []
            next_nodes = []
            for node in nodes:
                node_vals.append(node.val)
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            output.append( sum(node_vals) / len(node_vals) )
            nodes = next_nodes
        return output        
        



        