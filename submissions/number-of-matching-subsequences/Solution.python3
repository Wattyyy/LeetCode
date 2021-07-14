// https://leetcode.com/problems/number-of-matching-subsequences

from collections import defaultdict, deque
from typing import List
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        listed_words = [deque(word) for word in words]
        d = defaultdict(list)
        for word in listed_words:
            d[word[0]].append(word)

        for char in s:
            new = []
            for word in d[char]:
                word.popleft()
                if 0 < len(word):
                    new.append(word)
            del d[char]
            for new_word in new:
                d[new_word[0]].append(new_word)
        
        ans = len(words)
        for _, item in d.items():
            ans -= len(item)
        return ans

            

        