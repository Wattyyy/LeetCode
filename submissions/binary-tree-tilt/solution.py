# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def get_sum(self, node: Optional[TreeNode]) -> int:
        """
        1. return a subtree's sum containing an input node
        2. calculate a node's tilt value
        """
        if not node:
            return 0
        l_sub_sum, r_sub_sum = self.get_sum(node.left), self.get_sum(node.right)
        self.ans += abs(l_sub_sum - r_sub_sum)

        return node.val + l_sub_sum + r_sub_sum

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.get_sum(root)
        return self.ans
