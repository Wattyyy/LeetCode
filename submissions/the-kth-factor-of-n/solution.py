// https://leetcode.com/problems/the-kth-factor-of-n

from math import sqrt

class Solution:
    def kthFactor(self, n, k):
        factors = set()
        for a in range(1, int(sqrt(n)) + 1):
            if n % a == 0:
                factors.add(a)
                factors.add(int(n/a))
        factors = sorted(list(factors))
        if len(factors) < k:
            return -1
        else:
            return factors[k - 1]
        