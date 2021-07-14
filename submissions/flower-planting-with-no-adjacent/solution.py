// https://leetcode.com/problems/flower-planting-with-no-adjacent

from collections import defaultdict

class Solution:
    def gardenNoAdj(self, N, paths):
        ans = [0 for _ in range(N+1)]
        graph = defaultdict(list)
        color_map = defaultdict(int)
        for path in paths:
            u, v = path[0], path[1]
            graph[u].append(v)
            graph[v].append(u)

        # coloring
        color_set = set([1, 2, 3, 4])
        for v in range(1, N+1):
            used_color = set()
            neighbors = graph[v]
            for nv in neighbors:
                nv_color = color_map[nv]
                if nv_color == 0:
                    continue
                used_color.add(color_map[nv])
            available = list(color_set - used_color)
            color_map[v] = available[0]
            ans[v] = available[0]
            
        return ans[1:]