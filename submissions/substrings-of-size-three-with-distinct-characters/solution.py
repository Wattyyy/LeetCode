# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if i + 2 < len(s):
                sub = s[i] + s[i+1] + s[i+2]
                if len(set(sub)) == 3:
                    ans += 1
        return ans
                    
        