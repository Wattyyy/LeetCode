// https://leetcode.com/problems/prefix-and-suffix-search

from collections import defaultdict
from typing import List

class WordFilter:
    def __init__(self, words: List[str]):
        self.d = defaultdict(list)
        for i, word in enumerate(words):
            for j in range(1, len(word)+1):
                pre = word[:j]
                for k in range(len(word)):
                    suf = word[k:len(word)]
                    self.d[(pre, suf)].append(i)
        

    def f(self, prefix: str, suffix: str) -> int:
        if (prefix, suffix) in self.d:
            return self.d[(prefix, suffix)][-1]
        else:
            return -1

