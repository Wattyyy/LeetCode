// https://leetcode.com/problems/partition-array-for-maximum-sum

class Solution:
    def maxSumAfterPartitioning(self, A, K):
        A = [0] + A
        dp = [-1 for _ in range(len(A))]
        dp[0] = 0
        for i in range(1, len(A)):
            for k in range(1, K+1):
                if i-k>=0:
                    dp[i] = max(dp[i], dp[i-k] + k*max(A[i-k+1:i+1]))
        return dp[-1]
