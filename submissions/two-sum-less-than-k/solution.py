# https://leetcode.com/problems/two-sum-less-than-k

from bisect import bisect_left


class Solution:
    def twoSumLessThanK(self, A, K):
        if len(A) == 1:
            return -1
        ans = -1
        A = sorted(A)
        for i, a in enumerate(A):
            target = K - a
            idx = bisect_left(A, target)
            if i < idx - 1:
                ans = max(ans, A[i] + A[idx - 1])
        return ans
