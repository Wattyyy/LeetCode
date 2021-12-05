# https://leetcode.com/problems/longest-palindromic-subsequence

from collections import defaultdict
class Solution:
    def longestPalindromeSubseq(self, s):
        N = len(s)
        dp = defaultdict(int)
        for i in range(N):
            dp[(i, i)] = 1
            if (i+1 < N):
                if s[i] == s[i+1]:
                    dp[(i, i+1)] = 2
                else:
                    dp[(i, i+1)] = 1
        
        for i in reversed(range(N-2)):
            for j in range(i+2, N):
                if s[i] == s[j]:
                    dp[(i, j)] = dp[(i+1, j-1)] + 2
                else:
                    dp[(i, j)] = max(dp[(i, j-1)], dp[(i+1, j)])
        
        ans = 0
        for i in range(N):
            for j in range(N):
                ans = max(ans, dp[(i, j)])
        return ans
