# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num):
        if num==1:
            return True
        l, r = 0, num
        while l < r:
            mid = (l + r) // 2
            val = mid * mid
            if val == num:
                return True
            elif val < num:
                l = mid + 1
            else:
                r = mid
        return False
                
        
