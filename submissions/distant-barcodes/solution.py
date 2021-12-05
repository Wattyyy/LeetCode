# https://leetcode.com/problems/distant-barcodes

from collections import Counter
import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes):
        barcodes = [str(val) for val in barcodes]
        cnt = Counter(barcodes)
        max_heap = [(-val, key) for key, val in cnt.items()]
        heapq.heapify(max_heap)
        prev_v, prev_k = heapq.heappop(max_heap)
        ans = [prev_k]
        while len(ans) < len(barcodes):
            v, k = heapq.heappop(max_heap)
            ans.append(k)
            if prev_v + 1 < 0:
                heapq.heappush(max_heap, (prev_v + 1, prev_k))
            prev_v, prev_k = v, k
        return ans



