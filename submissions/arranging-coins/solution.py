# https://leetcode.com/problems/arranging-coins


class Solution:
    def arrangeCoins(self, n):
        k = 1
        while (k * (k + 1)) // 2 <= n:
            k += 1
        return k - 1
