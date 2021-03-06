# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n):
        dp = [float("inf") for _ in range(n+1)]
        dp[0], dp[1] = 0, 1
        x = 1
        while x * x <= n:
            dp[x*x] = 1
            x += 1

        for i in range(2, n+1):
            x = 1
            while x * x < i:
                val = x * x
                dp[i] = min(dp[i], dp[i-val] + dp[val])
                x += 1
        return dp[n]

