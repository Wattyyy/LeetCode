# https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation

from collections import defaultdict


class Solution:
    def reinitializePermutation(self, n: int) -> int:
        ls = [i for i in range(n)]
        key = tuple(ls)
        conv = defaultdict(int)
        for i in range(n):
            if i % 2 == 0:
                conv[i] = i // 2
            else:
                conv[i] = (n // 2) + (i - 1) // 2
        cnt = 0
        while True:
            new = ls[:]
            for i in range(n):
                new[i] = conv[new[i]]
            cnt += 1
            if tuple(new) == key:
                return cnt
            else:
                ls = new
