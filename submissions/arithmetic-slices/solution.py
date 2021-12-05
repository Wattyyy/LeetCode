# https://leetcode.com/problems/arithmetic-slices


class Solution:
    def numberOfArithmeticSlices(self, A):
        N = len(A)
        if N < 3:
            return 0
        dp = [0 for _ in range(N)]
        for i in range(2, N):
            if A[i - 1] - A[i - 2] == A[i] - A[i - 1]:
                dp[i] = dp[i - 1] + 1
        return sum(dp)
