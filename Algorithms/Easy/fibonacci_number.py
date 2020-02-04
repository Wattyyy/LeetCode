# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, N):
        dp = {}
        dp[0], dp[1] = 0, 1
        if N<=1:
            return dp[N]
        for n in range(2, N+1):
            dp[n] = dp[n-1] + dp[n-2]
        return dp[N]
        
