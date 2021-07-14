// https://leetcode.com/problems/valid-palindrome

import re
class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub('[^0-9a-z]', '', s)
        lp, rp = 0, len(s) - 1
        while lp <= rp:
            if s[lp] != s[rp]:
                return False
            lp += 1
            rp -= 1
        
        return True

        