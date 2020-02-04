# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, s):
        ls = list(s)
        ls.reverse()
        ans = 0
        for i in range(len(ls)):
            ans += (ord(ls[i]) - 64) * (26**i)
        return ans

