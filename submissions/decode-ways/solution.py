# https://leetcode.com/problems/decode-ways


class Solution:
    def numDecodings(self, s: str) -> int:
        valids = {str(i) for i in range(1, 27)}
        if len(s) == 1:
            res = 0
            if s in valids:
                res += 1
            return res
        if len(s) == 2:
            res = 0
            if s in valids:
                res += 1
            if s[0] in valids and s[1] in valids:
                res += 1
            return res

        dp = [0] * len(s)
        if s[0] in valids:
            dp[0] = 1
        if s[1] in valids:
            dp[1] += dp[0]
        if s[0] + s[1] in valids:
            dp[1] += 1

        for i in range(2, len(s)):
            if s[i] in valids:
                dp[i] += dp[i - 1]
            if s[i - 1] + s[i] in valids:
                dp[i] += dp[i - 2]
        return dp[-1]
