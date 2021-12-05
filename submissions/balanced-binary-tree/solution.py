# https://leetcode.com/problems/balanced-binary-tree


class Solution:
    def isBalanced(self, root):
        class NotBalanced(Exception):
            pass

        def is_balanced(node):
            if not node:
                return 0
            left, right = is_balanced(node.left), is_balanced(node.right)
            if abs(left - right) > 1:
                raise NotBalanced
            return max(left, right) + 1

        try:
            is_balanced(root)
            return True
        except NotBalanced:
            return False
