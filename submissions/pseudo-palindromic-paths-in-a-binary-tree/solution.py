# https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree

from collections import Counter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def backtrack(self, node, cnt):
        if not node.left and not node.right:
            tmp = 0
            for key in cnt:
                if cnt[key] % 2 == 1:
                    tmp += 1
            if tmp <= 1:
                self.ans += 1
            return 

        if node.left:
            cnt[node.left.val] += 1
            self.backtrack(node.left, cnt)
            cnt[node.left.val] -= 1

        if node.right:
            cnt[node.right.val] += 1
            self.backtrack(node.right, cnt)
            cnt[node.right.val] -= 1
        
    def pseudoPalindromicPaths (self, root):
        cnt = Counter()
        cnt[root.val] += 1
        self.backtrack(root, cnt)
        return self.ans
        