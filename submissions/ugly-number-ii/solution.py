import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        used = set()
        cnt = 0
        min_heap = [1]
        heapq.heapify(min_heap)
        while cnt < n:
            cnt += 1
            val = heapq.heappop(min_heap)
            used.add(val)
            for f in [2, 3, 5]:
                if val * f not in used:
                    used.add(val * f)
                    heapq.heappush(min_heap, val * f)

        return val
