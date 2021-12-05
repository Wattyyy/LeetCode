# https://leetcode.com/problems/top-k-frequent-words

from collections import defaultdict
class Solution:
    def topKFrequent(self, words, k):
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        l = []
        for word, freq in d.items():
            l.append((word, freq))
        l = sorted(l)
        l = sorted(l, key = lambda x: x[1], reverse = True)
        ans = []
        for item in l[:k]:
            ans.append(item[0])
        return ans