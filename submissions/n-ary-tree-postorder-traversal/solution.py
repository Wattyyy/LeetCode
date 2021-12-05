# https://leetcode.com/problems/n-ary-tree-postorder-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def postorder(self, root):
        if not root:
            return []
        st = deque([root])
        ans = []
        while st:
            node = st.pop()
            ans.append(node.val)
            if node.children:
                for child in node.children:
                    st.append(child)

        return ans[::-1]
