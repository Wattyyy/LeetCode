# https://leetcode.com/problems/student-attendance-record-i

from collections import Counter


class Solution:
    def checkRecord(self, s):
        cnt = Counter(s)
        return (cnt["A"] <= 1) and ("LLL" not in s)
