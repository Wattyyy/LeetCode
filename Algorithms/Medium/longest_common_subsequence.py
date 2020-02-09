# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1, text2):
        C = len(text1)
        R = len(text2)
        dp = [[0 for _ in range(C+1)] for __ in range(R+1)]
        text1 = " " + text1
        text2 = " " + text2
        for r in range(1, R+1):
            for c in range(1, C+1):
                if text2[r] == text1[c]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r-1][c], dp[r][c-1])
        return dp[R][C]
            
        
        
