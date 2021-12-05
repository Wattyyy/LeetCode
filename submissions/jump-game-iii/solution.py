# https://leetcode.com/problems/jump-game-iii

from collections import defaultdict


class Solution:
    def canReach(self, arr, start):
        N = len(arr)
        visited = [False for _ in range(N)]
        zero_ids = []
        for i in range(N):
            if arr[i] == 0:
                zero_ids.append(i)
        graph = defaultdict(list)
        for i in range(N):
            next_ids = [i + arr[i], i - arr[i]]
            for idx in next_ids:
                if 0 <= idx and idx < N:
                    graph[i].append(idx)
        # bfs
        queue = [start]
        while queue:
            idx = queue.pop(0)
            visited[idx] = True
            for next_id in graph[idx]:
                if visited[next_id] == False:
                    queue.append(next_id)

        for z_id in zero_ids:
            if visited[z_id]:
                return True
        return False
