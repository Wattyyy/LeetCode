# https://leetcode.com/problems/jump-game-iv

from collections import defaultdict
class Solution:
    def minJumps(self, arr):
        N = len(arr)
        if N==1:
            return 0
        if (arr[0] == arr[-1]) or N == 2:
            return 1
        if arr[0] == arr[-2]:
            return 2
        
        val2ids = defaultdict(list)
        for i in range(N):
            val2ids[arr[i]].append(i)
        
        graph = defaultdict(list)
        for i in range(N):
            tmp_set = set()
            if i==0:
                tmp_set.add(i+1)
            elif i==N-1:
                tmp_set.add(i-1)
            else:
                tmp_set.add(i+1)
                tmp_set.add(i-1)
            for item in val2ids[arr[i]]:
                tmp_set.add(item)
            tmp_set.remove(i)
            graph[i] = list(tmp_set)
        
        del val2ids
        # bfs
        dist = [float("inf") for _ in range(N)]
        dist[0] = 0
        queue = [0]
        while queue:
            idx = queue.pop(0)
            for next_idx in graph[idx]:
                if dist[idx]+1 < dist[next_idx]:
                    dist[next_idx] = dist[idx] + 1
                    queue.append(next_idx)
        return dist[-1]