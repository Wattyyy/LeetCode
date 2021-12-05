# https://leetcode.com/problems/relative-sort-array

from collections import Counter
class Solution:
    def relativeSortArray(self, arr1, arr2):
        counter = Counter(arr1)
        res, unseen = [], []
        for num in arr2:
            cnt = counter[num]
            for _ in range(cnt):
                res.append(num)
            del counter[num]
            
        keys = list(counter.keys())
        for key in keys:
            cnt = counter[key]
            for _ in range(cnt):
                unseen.append(key)
            del counter[key]
            
        unseen = sorted(unseen)
        res = res + unseen
        return res