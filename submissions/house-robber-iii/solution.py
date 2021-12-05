# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    @lru_cache
    def dp(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        if not node.left and not node.right:
            return node.val

        if not node.left:
            return max(
                node.val + self.dp(node.right.left) + self.dp(node.right.right),
                self.dp(node.right),
            )

        if not node.right:
            return max(
                node.val + self.dp(node.left.left) + self.dp(node.left.right),
                self.dp(node.left),
            )

        return max(
            node.val
            + self.dp(node.left.left)
            + self.dp(node.left.right)
            + self.dp(node.right.left)
            + self.dp(node.right.right),
            self.dp(node.left) + self.dp(node.right),
        )

    def rob(self, root: Optional[TreeNode]) -> int:
        return self.dp(root)
