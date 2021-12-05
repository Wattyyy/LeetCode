# https://leetcode.com/problems/maximum-product-of-word-lengths

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words = list(set(words))
        words2set = {word: set(word) for word in words}
        res = 0
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                st1, st2 = words2set[w1], words2set[w2]
                if i < j and st1.isdisjoint(st2):
                    res = max(res, len(w1) * len(w2))
        return res
