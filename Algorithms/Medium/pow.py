# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            x = 1 / x
            n = abs(n)
        res = 1.0
        while n:
            if n & 1:
                res = res * x
            x = x * x
            n = n >> 1
        return res
                
        
        
