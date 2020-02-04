# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x, n):
        def fastPow(x, n):
            if n==0:
                return 1.0
            half = fastPow(x, n//2):
            if n%2==0:
                return half * half
            else:
                return half * half * x
        
        if n<0:
            x = 1/x
            n = -n
        return fastPow(x, n)
