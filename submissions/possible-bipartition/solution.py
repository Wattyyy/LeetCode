# https://leetcode.com/problems/possible-bipartition

from collections import defaultdict, deque
class Solution:
    def possibleBipartition(self, N, dislikes):
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        color_arr = [0] * N
        for i in range(N):
            if color_arr[i] == 1 or color_arr[i] == -1:
                continue
            queue = deque([(i, 0)])
            while queue:
                v, prev = queue.popleft()
                if prev == 0 or prev == -1:
                    color_arr[v] = 1
                else:
                    color_arr[v] = -1
                for nv in graph[v]:
                    if color_arr[nv] == 0:
                        queue.append((nv, color_arr[v]))
                    elif color_arr[nv] == color_arr[v]:
                        return False
        
        return True
