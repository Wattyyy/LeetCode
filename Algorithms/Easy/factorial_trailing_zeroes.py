# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def __init__(self):
        self.ans = 0
        
    def count(self, n, m):
        val = n//m
        if val == 0:
            return
        self.ans += val
        self.count(n, m*5)
        
    def trailingZeroes(self, n):
        self.count(n, 5)
        return self.ans
