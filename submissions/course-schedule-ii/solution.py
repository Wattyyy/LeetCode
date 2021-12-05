# https://leetcode.com/problems/course-schedule-ii

from collections import deque, defaultdict


class Solution:
    def topological_sort(self, n, graph):
        in_order = [0 for _ in range(n)]
        for i in graph:
            for j in graph[i]:
                in_order[j] += 1
        queue = deque([])
        for i in range(n):
            if in_order[i] == 0:
                queue.append(i)
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
        if cnt != n:
            return []
        else:
            return res

    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for v, u in prerequisites:
            graph[u].append(v)
        return self.topological_sort(numCourses, graph)
