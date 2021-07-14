// https://leetcode.com/problems/counting-elements

from collections import Counter
class Solution:
    def countElements(self, arr):
        st = set(arr)
        res = 0
        for num in arr:
            if num + 1 in st:
                res += 1
        return res
            