# https://leetcode.com/problems/shortest-path-with-alternating-colors

from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        graph = defaultdict(list)
        for u, v in red_edges:
            graph[u].append([v, "R"])
        for u, v in blue_edges:
            graph[u].append([v, "B"])
        ans = [float("inf")] * n
        visited = set()
        queue = deque([(0, 0, "N")])
        while queue:
            node, count, color = queue.popleft()
            ans[node] = min(ans[node], count)
            visited.add((node, color))
            for nx_node, nx_color in graph[node]:
                if nx_color == color or (nx_node, nx_color) in visited:
                    continue
                queue.append((nx_node, count + 1, nx_color))
        for i, a in enumerate(ans):
            if a == float("inf"):
                ans[i] = -1
        return ans
