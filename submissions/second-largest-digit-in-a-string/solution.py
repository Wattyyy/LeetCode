# https://leetcode.com/problems/second-largest-digit-in-a-string


class Solution:
    def secondHighest(self, s: str) -> int:
        st = set()
        nums = {str(i) for i in range(10)}
        for i, char in enumerate(s):
            if char in nums:
                st.add(char)
        ls = sorted(list(st), reverse=True)
        if len(ls) < 2:
            return -1
        else:
            return ls[1]
