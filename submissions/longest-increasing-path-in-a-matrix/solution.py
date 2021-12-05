# https://leetcode.com/problems/longest-increasing-path-in-a-matrix

from collections import defaultdict, deque


class Solution:
    def topological_sort(self, graph):
        in_order = {key: 0 for key in graph}
        for key1 in graph:
            for key2 in graph[key1]:
                in_order[key2] += 1
        queue = deque([])
        for key in in_order:
            if in_order[key] == 0:
                queue.append(key)
        cnt = 0
        res = []
        while queue:
            v = queue.popleft()
            res.append(v)
            for neighbor in graph[v]:
                in_order[neighbor] -= 1
                if in_order[neighbor] == 0:
                    queue.append(neighbor)
            cnt += 1
        return res

    def longestIncreasingPath(self, matrix):
        graph = defaultdict(list)
        R, C = len(matrix), len(matrix[0])
        dist = {}
        for r in range(R):
            for c in range(C):
                graph[(r, c)] = []
                dist[(r, c)] = -1
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if (
                        (0 <= nr < R)
                        and (0 <= nc < C)
                        and (matrix[r][c] < matrix[nr][nc])
                    ):
                        graph[(r, c)].append((nr, nc))

        N = len(graph)
        order = self.topological_sort(graph)

        def dfs(key, cnt):
            if cnt <= dist[key]:
                return
            dist[key] = cnt
            for next_key in graph[key]:
                dfs(next_key, cnt + 1)

        for key in order:
            dfs(key, 0)

        return max(dist.values()) + 1
