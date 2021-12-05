# https://leetcode.com/problems/perfect-squares

class Solution:
    def numSquares(self, n):
        dp = [float('inf')] * (n + 1)
        dp[0], dp[1] = 0, 1
        i = 1
        while i * i <= n:
            dp[i * i] = 1
            i += 1
            
        for i in range(2, n+1):
            j = 1
            while j * j < i:
                val = j * j 
                dp[i] = min(dp[i], dp[i - val] + 1)
                j += 1
        return dp[-1]
