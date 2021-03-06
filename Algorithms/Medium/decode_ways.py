# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s):
        N = len(s)
        if s == "0":
            return 0
        if N == 0 or N == 1:
            return N
        
        # avoid index error
        s = " " +  s
        dp = [0 for _ in range(len(s))]
        dp[0] = 1
        dp[1] = 0 if s[1] == "0" else 1
        for i in range(2, len(s)):
            if s[i] != "0":
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) and int(s[i-1:i+1]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

