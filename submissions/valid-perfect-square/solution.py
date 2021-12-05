# https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num):
        if num == 1:
            return True
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 == num:
                return True
            elif mid **2 < num:
                l = mid + 1
            else:
                r = mid - 1
        return False
            
        