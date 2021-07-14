// https://leetcode.com/problems/to-lower-case

class Solution:
    def toLowerCase(self, s: str) -> str:
        res = []
        for char in s:
            if 65 <= ord(char) <= 90:
                res.append( chr(ord(char) + 32) )
            else:
                res.append(char)
        return ''.join(res)
        