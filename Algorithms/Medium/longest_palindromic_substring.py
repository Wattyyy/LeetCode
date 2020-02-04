# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s):
        if not s:
            return
        N = len(s)
        if N==1 or (N==2 and s[0]==s[1]):
            return s
        if N==2 and s[0]!=s[1]:
            return s[0]
        
        dp = [[False for _ in range(N)] for __ in range(N)]
        for i in range(N):
            dp[i][i] = True
            if i!=(N-1) and s[i]==s[i+1]:
                dp[i][i+1] = True
        for i in reversed(range(N-1)):
            for j in range(i, N-1):
                if dp[i][j] and s[i-1]==s[j+1]:
                    dp[i-1][j+1] = True
        
        ans = [1, [0, 0]]
        for i in range(N):
            for j in range(N):
                if dp[i][j] and ans[0]<(j-i+1):
                    ans[0] = max(j-i+1, ans[0])
                    ans[1] = [i, j]
        i, j = ans[1][0], ans[1][1]
        return s[i:j+1]
        
        
