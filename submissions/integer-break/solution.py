// https://leetcode.com/problems/integer-break

class Solution:
    def integerBreak(self, n):
        if n <= 3:
            return n - 1
        dp = [0] * (59)
        dp[1], dp[2], dp[3] = 1, 2, 3
        for num in range(4, 59):
            for i in range(1, num):
                dp[num] = max(dp[num], (num - i) * dp[i])
        return dp[n]