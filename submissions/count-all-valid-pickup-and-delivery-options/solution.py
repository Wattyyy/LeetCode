class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = (((i * 2) * (i * 2 - 1) // 2) * dp[i - 1]) % MOD
        return dp[n]
