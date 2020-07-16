# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n):
        p, ans = 1, 0
        while 0 < n // (5 ** p):
            ans += n // (5 ** p)
            p += 1
        return ans
        
