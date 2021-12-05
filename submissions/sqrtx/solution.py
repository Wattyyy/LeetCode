# https://leetcode.com/problems/sqrtx


class Solution:
    def mySqrt(self, x):
        l, r = 0, x
        while l < r:
            mid = (l + r) // 2
            val = mid * mid
            if val == x:
                return mid
            elif val < x:
                l = mid + 1
            else:
                r = mid - 1
        if l * l > x:
            return l - 1
        else:
            return l
