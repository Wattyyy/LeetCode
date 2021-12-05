# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero

class Solution:
    def numberOfSteps (self, num):
        ans = 0
        while 0 < num:
            if num%2==0:
                num = num//2
            else:
                num -= 1
            ans += 1
        return ans
        