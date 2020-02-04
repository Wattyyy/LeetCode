# https://leetcode.com/problems/2-keys-keyboard/submissions/

class Solution:
    def minSteps(self, n):
        dp = [float("inf") for _ in range(n+1)]
        dp[0], dp[1] = 0, 0
        for i in range(1, n):
            if 2 * i > n:
                continue
            if dp[i] + 2 > dp[2*i]:
                continue
            dp[2 * i] = dp[i] + 2
            idx = 2 * i + i
            while idx <= n:
                dp[idx] = dp[idx - i] + 1
                idx += i
        return dp[n]
            
