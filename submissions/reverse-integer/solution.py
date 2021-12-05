# https://leetcode.com/problems/reverse-integer


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            res = -1 * int(str(abs(x))[::-1])
            if res < -1 * (2 ** 31):
                return 0
            else:
                return res
        else:
            res = int(str(abs(x))[::-1])
            if 2 ** 31 - 1 < res:
                return 0
            else:
                return res
