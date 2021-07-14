// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


import sys
sys.setrecursionlimit(10 ** 6)
class Solution:
    def maxSumBST(self, root):
        if not root:
            return 0
        self.ans = 0
        def dp(node):
            """ Calculate maximum sum using input node.
            @returns
                bst_sum: int  - Maximum sum.
                is_bst:  bool - Subtree including input node is BST or not BST.
                min_val: int  - Minimum value of subtree including input node
                max_val: int  - Maximum value of subtree including input node
            """

            if not node.left and not node.right:
                self.ans = max(self.ans, node.val)
                return node.val, True, node.val, node.val
                
            elif node.left and not node.right:
                l_sum, is_bst, min_val, max_val = dp(node.left)
                if is_bst and max_val < node.val:
                    self.ans = max(self.ans, l_sum + node.val)
                    return l_sum + node.val, True, min_val, node.val
                else:
                    return 0, False, 0, 0

            elif not node.left and node.right:
                r_sum, is_bst, min_val, max_val = dp(node.right)
                if is_bst and node.val < min_val:
                    self.ans = max(self.ans, node.val + r_sum)
                    return node.val + r_sum, True, node.val, max_val
                else:
                    return 0, False, 0, 0

            else:
                l_sum, l_is_bst, l_min_val, l_max_val = dp(node.left)
                r_sum, r_is_bst, r_min_val, r_max_val = dp(node.right)
                if l_is_bst and r_is_bst and l_max_val < node.val and node.val < r_min_val:
                    self.ans = max(self.ans, l_sum + node.val + r_sum)
                    return l_sum + node.val + r_sum, True, l_min_val, r_max_val
                else:
                    return 0, False, 0, 0
            
        dp(root)
        return self.ans
                
                
