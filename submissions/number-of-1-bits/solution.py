# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n):
        string = bin(n)[2:]
        ans = 0
        for s in string:
            if s=="1":
                ans += 1
        return ans
            