# https://leetcode.com/problems/longest-common-subsequence


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        R, C = len(text1), len(text2)
        if R == 0 or C == 0:
            return 0
        dp = [[0 for _ in range(C + 1)] for __ in range(R + 1)]
        text1 = " " + text1
        text2 = " " + text2
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                if text1[r] == text2[c]:
                    dp[r][c] = max(dp[r][c], dp[r - 1][c - 1] + 1)
                dp[r][c] = max(dp[r][c], dp[r - 1][c], dp[r][c - 1])
        return dp[-1][-1]
