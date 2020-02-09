# https://leetcode.com/problems/longest-palindromic-substring/

from collections import defaultdict
class Solution:
    def longestPalindrome(self, s):
        N = len(s)
        if N==0:
            return ""
        
        dp = defaultdict(bool)
        for i in range(N):
            dp[(i, i)] = True
            if (i+1 < N) and (s[i] == s[i+1]):
                dp[(i, i+1)] = True
        
        for i in reversed(range(N-2)):
            for j in range(i+2, N):
                if (dp[(i+1, j-1)]) and (s[i] == s[j]):
                    dp[(i, j)] = True
        
        max_len = 0
        res = ""
        for i in range(N):
            for j in range(i, N):
                if (dp[(i, j)]) and (max_len < j-i+1):
                    max_len = j-i+1
                    res = s[i:j+1]
        return res
