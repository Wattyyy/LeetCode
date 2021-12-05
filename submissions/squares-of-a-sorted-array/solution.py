# https://leetcode.com/problems/squares-of-a-sorted-array

from collections import deque
class Solution:
    def sortedSquares(self, A):
        ans = deque([])
        lp, rp = 0, len(A) - 1
        while lp <= rp:
            L, R = A[lp] ** 2, A[rp] ** 2
            if lp == rp:
                ans.appendleft(L)
                break
            if L < R:
                ans.appendleft(R)
                rp -= 1
            else:
                ans.appendleft(L)
                lp += 1
        return ans
                

            
