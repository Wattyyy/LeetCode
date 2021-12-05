# https://leetcode.com/problems/sort-characters-by-frequency

from collections import Counter, defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        val2key = defaultdict(list)
        for key, val in counter.items():
            val2key[val].append(key)
        vals = sorted(list(val2key.keys()), reverse=True)
        ans = []
        for v in vals:
            for char in val2key[v]:
                for _ in range(v):
                    ans.append(char)
        return ''.join(ans)






        