# https://leetcode.com/problems/palindromic-substrings/

from collections import defaultdict
class Solution:
    def countSubstrings(self, s):
        N = len(s)
        dp = defaultdict(bool)
        for i in range(N):
            dp[(i, i)] = True
            if (i + 1 < N) and (s[i] == s[i+1]):
                dp[(i, i+1)] = True
        for i in reversed(range(N)):
            for j in range(i+2, N):
                if (s[i] == s[j]) and dp[(i+1, j-1)]:
                    dp[(i, j)] = True
        
        ans = 0
        for i in range(N):
            for j in range(i, N):
                if dp[(i, j)]:
                    ans += 1
        return ans

