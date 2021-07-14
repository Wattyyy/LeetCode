// https://leetcode.com/problems/maximize-number-of-nice-divisors

class Solution:
    def maxprod(self, n):
        MOD = 10 ** 9 + 7
        if n == 1:
            return 1
        if n == 2:
            return 2
        elif n == 3:
            return 3
        d = n // 3
        res = n % 3
        if res == 0:
            res = 3
            return res * pow(3, d - 1, MOD) % MOD
        elif res == 1:
            res = 4
            return res * pow(3, d - 1, MOD) % MOD
        else:
            return res * pow(3, d, MOD) % MOD

    def maxNiceDivisors(self, primeFactors: int) -> int:
        res = self.maxprod(primeFactors)
        return res
   