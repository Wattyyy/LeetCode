class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        R, C = len(t), len(s)
        dp = [[0 for _ in range(C)] for __ in range(R)]
        cum_sum = [[0 for _ in range(C)] for __ in range(R)]
        for r in range(R):
            for c in range(C):
                if t[r] == s[c]:
                    dp[r][c] = 1

        for r in range(R):
            for c in range(r, C):
                if r == 0:
                    cum_sum[r][c] += dp[r][c]
                    if 0 < c:
                        cum_sum[r][c] += cum_sum[r][c - 1]
                else:
                    if dp[r][c] == 1:
                        cum_sum[r][c] += cum_sum[r - 1][c - 1]
                    cum_sum[r][c] += cum_sum[r][c - 1]
        return cum_sum[-1][-1]
