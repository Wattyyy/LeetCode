# https://leetcode.com/problems/zigzag-conversion


class Solution:
    def convert(self, s, n):
        ans = ""

        if len(s) == 1 or len(s) == 0 or len(s) <= n or n == 1:
            return s

        iter = 0
        while True:
            try:
                ans += s[(2 * n - 2) * iter]
            except IndexError:
                break
            iter += 1

        for i in range(1, n - 1):
            iter = 0
            while True:
                try:
                    number = i + (2 * n - 2) * iter
                    ans += s[number]
                except IndexError:
                    break
                try:
                    number = (2 * n - 2) - i + (2 * n - 2) * iter
                    ans += s[number]
                except IndexError:
                    break
                iter += 1

        iter = 0
        while True:
            try:
                ans += s[(n - 1) + (2 * n - 2) * iter]
            except IndexError:
                break
            iter += 1

        return ans
