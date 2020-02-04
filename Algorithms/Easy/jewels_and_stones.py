# https://leetcode.com/problems/jewels-and-stones/submissions/

class Solution:
    def numJewelsInStones(self, J, S):
        jewels = set()
        ans = 0
        for j in J:
            jewels.add(j)
        for s in S:
            if s in jewels:
                ans += 1
        return ans
         
