# https://leetcode.com/problems/reorganize-string

from math import ceil
from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S):
        Length = len(S)
        cnt = Counter(S)
        capacity = ceil(Length / 2)
        max_heap = [(-value, key) for key, value in cnt.items()]
        max_freq = cnt.most_common(1)[0][1]
        if capacity < max_freq:
            return ""
        
        heapq.heapify(max_heap)
        prev_v, prev_k = heapq.heappop(max_heap)
        ans = [prev_k]
        while len(ans) < Length:
            v, k = heapq.heappop(max_heap)
            ans.append(k)
            if prev_v + 1 <= 0:
                heapq.heappush(max_heap, (prev_v + 1, prev_k))
            prev_v, prev_k = v, k
        
        return "".join(ans)