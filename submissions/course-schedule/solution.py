# https://leetcode.com/problems/course-schedule

from collections import defaultdict, deque
class Solution:
    def topological_sort(self, graph, N):
        in_degree = [0] * N
        for i in range(N):
            for v in graph[i]:
                in_degree[v] += 1
        queue = deque([])
        for i in range(N):
            if in_degree[i] == 0:
                queue.append(i)
        cnt = 0
        res = []
        while queue:
            v = queue.popleft()
            for nv in graph[v]:
                in_degree[nv] -= 1
                if in_degree[nv] == 0:
                    queue.append(nv)
            res.append(v)
            cnt += 1
        if cnt != N:
            return []
        else:
            return res

    
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        for v, u in prerequisites:
            graph[u].append(v)
        res = self.topological_sort(graph, numCourses)
        return len(res) == numCourses
        
        