// https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        lp, rp = 0, len(s) - 1
        while lp <= rp:
            s[lp], s[rp] = s[rp], s[lp]
            lp += 1
            rp -= 1

        