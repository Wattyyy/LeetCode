# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s):
        N = len(s)
        dp = [[False for _ in range(N)] for __ in range(N)]
        for i in range(N):
            dp[i][i] = True
        for l in reversed(range(N-1)):
            for r in range(l+1, N):
                if (r - l == 1) and (s[l] == s[r]):
                    dp[l][r] = True
                elif (s[l] == s[r]) and dp[l+1][r-1]:
                    dp[l][r] = True
        
        ans = [0, '']
        for l in range(N):
            for r in range(l, N):
                if dp[l][r] and (ans[0] < r - l + 1):
                    ans[0] = r - l + 1
                    ans[1] = s[l:r+1]
        return ans[1]
                
                    
