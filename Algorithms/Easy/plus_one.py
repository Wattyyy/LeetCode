# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits):
        digits[-1] += 1
        i = len(digits)-1
        while i>0:
            if digits[i]==10:
                str_val = str(digits[i])
                digits[i] = int(str_val[1])
                digits[i-1] += 1
            i -= 1
        if digits[0]==10:
            digits[0] = 0
            digits = [1] + digits
        return digits
        
        
