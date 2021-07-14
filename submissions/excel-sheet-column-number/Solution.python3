// https://leetcode.com/problems/excel-sheet-column-number

class Solution:
    def titleToNumber(self, s):
        char2int = {chr(64 + i): i for i in range(1, 27)}
        s = s[::-1]
        ans = 0
        for i, char in enumerate(s):
            num = char2int[char]
            ans += num * (26 ** i)
        return ans