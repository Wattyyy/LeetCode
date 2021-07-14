// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n):
        dp = [0] * 46
        dp[0], dp[1] = 1, 1
        for i in range(2, 46):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
        
        