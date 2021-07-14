// https://leetcode.com/problems/consecutive-numbers-sum

from math import sqrt
class Solution:
    def consecutiveNumbersSum(self, N):
        u_lim = int( (sqrt(1 + 8 * N) - 1) / 2)
        ans = 0
        for i in range(1, u_lim+1):
            val = (N - i * (i + 1) // 2)
            if val % i == 0:
                ans += 1
        return ans
