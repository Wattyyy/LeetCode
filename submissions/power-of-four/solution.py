# https://leetcode.com/problems/power-of-four


class Solution:
    def isPowerOfFour(self, num):
        if num <= 0:
            return False
        while 1 < num:
            if num % 4 != 0:
                return False
            num = num // 4

        return True
