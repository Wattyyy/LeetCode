# https://leetcode.com/problems/search-suggestions-system

from collections import defaultdict
from typing import List


class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.words = []


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        root = Trie()
        for word in products:
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = Trie()
                cur = cur.children[char]
                cur.words.append(word)

        cur = root
        res = []
        for i, char in enumerate(searchWord):
            if char in cur.children:
                cur = cur.children[char]
                res.append(sorted(cur.words)[:3])
            else:
                for _ in range(len(searchWord) - i):
                    res.append([])
                break
        return res
