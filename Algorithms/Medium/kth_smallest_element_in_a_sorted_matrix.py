# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

from bisect import bisect_right
class Solution:
    def kthSmallest(self, matrix, k):
        N, M = len(matrix), len(matrix[0])
        l, r = matrix[0][0], matrix[-1][-1]
        while l < r:
            mid = l + (r - l) // 2 
            cnt = 0
            for m in range(M):
                cnt += bisect_right(matrix[m], mid)
            if k <= cnt:
                r = mid
            else:
                l = mid + 1
        return r

        
