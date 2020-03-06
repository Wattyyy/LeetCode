# https://leetcode.com/problems/super-pow/

class Solution:
    def superPow(self, a, b):
        res = 1
        num = int("".join(list(map(str, b))))
        while num > 0:
            if num & 1:
                res = res * a % 1337
            a = a * a % 1337
            num = num >> 1
        return res
