# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def d_and_c(self, nums: List[int]) -> None:
        N = len(nums)
        if N == 0:
            return None
        node = TreeNode(nums[N // 2])
        node.left = self.d_and_c(nums[: N // 2])
        node.right = self.d_and_c(nums[1 + N // 2 :])
        return node

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        root = self.d_and_c(nums)
        return root
