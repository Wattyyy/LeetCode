# https://leetcode.com/problems/global-and-local-inversions


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all([abs(i - a) <= 1 for (i, a) in enumerate(A)])
