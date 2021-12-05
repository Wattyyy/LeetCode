# https://leetcode.com/problems/most-common-word

from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph, banned):
        symbols = ["!", "?", "'", ",", ";", "."]
        for symbol in symbols:
            paragraph = paragraph.replace(symbol, " ")
        paragraph = paragraph.lower()
        cntr = Counter(paragraph.split(" "))
        for key in banned:
            if key in cntr:
                del cntr[key]
        if "" in cntr:
            del cntr[""]
        ans = [None, 0]
        for k, v in cntr.items():
            if ans[1] < v:
                ans[0], ans[1] = k, v
        return ans[0]
