# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x):
        str_x = str(x)
        rev = ""
        for s in str_x:
            rev = s + rev             
        if str_x == rev:
            return True
        else:
            return False