// https://leetcode.com/problems/hamming-distance

class Solution:
    def hammingDistance(self, x, y):
        res = 0
        xor = x ^ y
        while 0 < xor:
            res += (xor & 1)
            xor = xor >> 1
        return res
            