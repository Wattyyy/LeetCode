# https://leetcode.com/problems/power-of-two


class Solution:
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 == 1:
            return False
        return self.isPowerOfTwo(n // 2)
