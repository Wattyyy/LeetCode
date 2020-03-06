# https://leetcode.com/problems/sort-characters-by-frequency/

from collections import Counter
class Solution:
    def frequencySort(self, s):
        cnt = Counter(s)
        ans = []
        for k, v in sorted(cnt.items(), key = lambda item: item[1], reverse = True):
            ans.append(k * v)
        return "".join(ans)


