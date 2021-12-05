# https://leetcode.com/problems/find-lucky-integer-in-an-array

from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        ans = -1
        for k, v in cnt.items():
            if k == v:
                ans = max(ans, k)
        return ans