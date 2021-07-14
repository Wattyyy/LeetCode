// https://leetcode.com/problems/increasing-decreasing-string

import heapq
from collections import Counter

class Solution:
    def sortString(self, s):
        num_list = [ord(char)-60 for char in s]
        num_cnt = Counter(num_list)

        res = []
        while num_cnt.keys():

            min_heap = list(num_cnt.keys())
            heapq.heapify(min_heap)
            while min_heap:
                num = heapq.heappop(min_heap)
                num_cnt[num] -= 1
                if num_cnt[num] == 0:
                    del num_cnt[num]
                res.append(chr(num + 60))

            max_heap = [-num for num in num_cnt.keys()]
            heapq.heapify(max_heap)
            while max_heap:
                num = heapq.heappop(max_heap)
                num = abs(num)
                num_cnt[num] -= 1
                if num_cnt[num] == 0:
                    del num_cnt[num]
                res.append(chr(num + 60))
        
        return ''.join(res)
            

        
