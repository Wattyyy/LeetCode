# https://leetcode.com/problems/parallel-courses

from collections import defaultdict, deque


class Solution:
    def topological_sort(self, n, graph):
        in_order = [0 for _ in range(n)]
        for i in graph:
            for j in graph[i]:
                in_order[j] += 1
        queue = deque([])
        for i in range(n):
            if in_order[i] == 0:
                queue.append((i, 1))
        cnt, res = 0, 0
        while queue:
            node, val = queue.popleft()
            res = max(res, val)
            for neighbor in graph[node]:
                in_order[neighbor] -= 1
                if in_order[neighbor] == 0:
                    queue.append((neighbor, val + 1))
            cnt += 1
        if cnt != n:
            return -1
        return res

    def minimumSemesters(self, N, relations):
        graph = defaultdict(list)
        for u, v in relations:
            graph[u - 1].append(v - 1)
        res = self.topological_sort(N, graph)
        if res == -1:
            return -1
        return res
