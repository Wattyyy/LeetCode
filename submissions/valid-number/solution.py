# https://leetcode.com/problems/valid-number


class Solution:
    def isNumber(self, s: str) -> bool:
        invalids = {"inf", "-inf", "+inf", "Infinity", "-Infinity", "+Infinity"}
        if s in invalids:
            return False
        try:
            res = float(s)
            return True
        except ValueError:
            return False
