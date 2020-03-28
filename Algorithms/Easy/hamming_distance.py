# https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x, y):
        xor = x ^ y
        res = 0
        while xor:
            if xor & 1:
                res += 1
            xor = xor >> 1
        return res
        
