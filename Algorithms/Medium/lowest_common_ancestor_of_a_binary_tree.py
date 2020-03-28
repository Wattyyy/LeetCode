# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from copy import deepcopy

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        pv, qv = p.val, q.val
        self.dic = {pv:[], qv:[]}
        def backtrack(target, node=root, current=[(root, root.val)]):
            if len(self.dic[target]) == 1:
                return
            elif node.val == target:
                self.dic[target].append(deepcopy(current))
            else:
                if node.left:
                    current.append((node.left, node.left.val))
                    backtrack(target, node.left, current)
                    current.pop()
                if node.right:
                    current.append((node.right, node.right.val))
                    backtrack(target, node.right, current)
                    current.pop()

        backtrack(target=pv)
        backtrack(target=qv)
        
        p_list, q_list = self.dic[pv][0], self.dic[qv][0]
        N = min(len(p_list), len(q_list))
        i = 0
        ans = root
        while i < N:
            if p_list[i][1] == q_list[i][1]:
                ans = p_list[i][0]
                i += 1
            else:
                break

        return ans

