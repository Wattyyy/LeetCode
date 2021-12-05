# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s):
        N = len(s)
        dp = [[False for _ in range(N)] for __ in range(N)]
        for i in range(N):
            dp[i][i] = True
        for i in reversed(range(N-1)):
            for j in range(i+1, N):
                if i + 1 < j:
                    if dp[i+1][j-1] and s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        dp[i][j] = True
        ans_idx = [0, 0]
        for i in range(N):
            for j in range(i, N):
                if dp[i][j] and (ans_idx[1] - ans_idx[0] < j - i):
                    ans_idx[0], ans_idx[1] = i, j
        l, r = ans_idx[0], ans_idx[1]
        return s[l:r+1]


        