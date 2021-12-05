# https://leetcode.com/problems/backspace-string-compare


class Solution:
    def triming(self, string):
        res = []
        for char in string:
            if char == "#":
                if 1 <= len(res):
                    res.pop(-1)
                else:
                    continue
            else:
                res.append(char)
        return res

    def backspaceCompare(self, S, T):
        s, t = self.triming(S), self.triming(T)
        return s == t
