# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

from collections import defaultdict
class Solution:
    def findSpecialInteger(self, arr):
        cnt_dic = defaultdict(int)
        for i in range(len(arr)):
            cnt_dic[arr[i]] += 1
        for k, v in cnt_dic.items():
            if v / len(arr) > 0.25:
                return k
            
