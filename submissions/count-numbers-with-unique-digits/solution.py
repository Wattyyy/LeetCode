# https://leetcode.com/problems/count-numbers-with-unique-digits


class Solution:
    def countNumbersWithUniqueDigits(self, n):
        if n == 0:
            return 1
        # key: n, value: count
        # count unique for 10**(n-1) <= x < 10**(n)
        d = {}
        d[1], d[2] = 10, 81
        for i in range(3, 11):
            d[i] = d[i - 1] * (11 - i)
        for i in range(2, 11):
            d[i] = d[i] + d[i - 1]

        if n > 10:
            return d[10]
        else:
            return d[n]
