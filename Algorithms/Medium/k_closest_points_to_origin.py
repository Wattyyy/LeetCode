# https://leetcode.com/problems/k-closest-points-to-origin/

from collections import defaultdict, Counter
class Solution:
    def kClosest(self, points, K):
        p2d = defaultdict(int)
        p2c = defaultdict(int)
        for x, y in points:
            p2d[(x, y)] = (x ** 2) + (y ** 2)
            p2c[(x, y)] += 1

        ans = []
        sorted_p2d = sorted(p2d.items(), key=lambda item: item[1])
        for item in sorted_p2d:
            point = item[0]
            cnt = p2c[point]
            for _ in range(cnt):
                ans.append(list(point))

        if K < len(ans):
            for _ in range(len(ans) - K):
                ans.pop()
        return ans

        
