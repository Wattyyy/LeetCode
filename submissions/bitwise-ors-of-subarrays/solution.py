# https://leetcode.com/problems/bitwise-ors-of-subarrays


class Solution:
    def subarrayBitwiseORs(self, A):
        ans = {A[0]}
        cur = {A[0]}
        for i, a in enumerate(A):
            if i == 0:
                continue
            new = set()
            for v in cur:
                new.add(v | a)
            new.add(a)
            cur = new
            ans |= cur
        return len(ans)
