# https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits):
        if not digits:
            return []
        digits[-1] += 1
        for i in reversed(range(1, len(digits))):
            if digits[i]==10:
                digits[i] = 0
                digits[i-1] += 1
            else:
                continue
        if digits[0]==10:
            digits[0] = 0
            digits = [1] + digits
        return digits
            