# https://leetcode.com/problems/decode-ways-ii

from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:
        M = 10 ** 9 + 7
        valids = defaultdict(int)
        valids['*'], valids['1*'], valids['2*'], valids['**'] = 9, 9, 6, 15
        for i in range(1, 27):
            valids[str(i)] = 1
        for i in range(10):
            key = '*' + str(i)
            if i <= 6:
                valids[key] = 2
            else:
                valids[key] = 1
        
        dp = defaultdict(int)
        dp[0] = valids[s[0]]
        if dp[0] != 0:
            dp[-1] = 1
        
        for i in range(1, len(s)):
            key1 = s[i]
            key2 = s[i-1] + s[i]
            dp[i] = (dp[i-1] * valids[key1]) % M + (dp[i-2] * valids[key2]) % M
            dp[i] = dp[i] % M
            
        
        return dp[len(s)-1]
            
        
        