// https://leetcode.com/problems/jewels-and-stones

from collections import Counter
class Solution:
    def numJewelsInStones(self, J, S):
        cnt = Counter(S)
        ans = 0
        for char in J:
            ans += cnt[char]
        return ans
        