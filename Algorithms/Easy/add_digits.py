# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num):
        if num==0:
            return 0
        if num%9 == 0:
            return 9
        while True:
            if num < 10:
                return num
            num = num % 9
