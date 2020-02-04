# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n):
        dp = {}
        dp[1], dp[2] = 1, 2
        if n<=2:
            return dp[n]
        for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[n]
        
