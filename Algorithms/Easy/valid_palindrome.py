# https://leetcode.com/problems/valid-palindrome/

import re
class Solution:
    def isPalindrome(self, s):
        if not s: 
            return True
        s_list = []
        for char in s:
            if re.match(r'[a-zA-Z0-9]', char):
                s_list.append(char.lower())
                
        lp, rp = 0, len(s_list) - 1
        while lp <= rp:
            if s_list[lp] != s_list[rp]:
                return False
            lp += 1
            rp -= 1
        return True
