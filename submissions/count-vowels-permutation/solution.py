# https://leetcode.com/problems/count-vowels-permutation

from collections import defaultdict


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 10 ** 9 + 7
        dp = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        for _ in range(n - 1):
            new = defaultdict(int)
            new["a"] = (dp["e"] + dp["i"] + dp["u"]) % M
            new["e"] = (dp["a"] + dp["i"]) % M
            new["i"] = (dp["e"] + dp["o"]) % M
            new["o"] = dp["i"] % M
            new["u"] = (dp["i"] + dp["o"]) % M
            dp = new

        return sum(dp.values()) % M
