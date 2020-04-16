# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n):
        appear = set([n])
        num = n
        while num != 1:
            str_num = str(num)
            num = 0
            for sn in str_num:
                num += pow(int(sn), 2)
            if num in appear:
                return False
            else:
                appear.add(num)
        return True

