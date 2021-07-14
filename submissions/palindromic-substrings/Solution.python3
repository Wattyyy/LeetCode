// https://leetcode.com/problems/palindromic-substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [[False for _ in range(N)] for __ in range(N)]
        for i in range(N):
            dp[i][i] = True
        for i in reversed(range(N)):
            for j in range(i+1, N):
                if j - i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                else:
                    if dp[i+1][j-1] and s[i] == s[j]:
                        dp[i][j] = True
        
        ret = 0
        for i in reversed(range(N)):
            for j in range(i, N):
                if dp[i][j]:
                    ret += 1
        return ret
