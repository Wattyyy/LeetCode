# https://leetcode.com/problems/walls-and-gates/

from collections import deque
class Solution:
    def wallsAndGates(self, rooms):
        if not rooms:
            return None
        M, N = len(rooms), len(rooms[0])
        def bfs(m, n):
            vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            queue = deque([(m, n)])
            while queue:
                y_1, x_1 = queue.popleft()
                for vec in vectors:
                    y_2 = y_1 + vec[0]
                    x_2 = x_1 + vec[1]
                    if 0<=y_2 and y_2<M and 0<=x_2 and x_2<N and rooms[y_1][x_1]<rooms[y_2][x_2]:
                        queue.append((y_2, x_2))
                        rooms[y_2][x_2] = rooms[y_1][x_1] + 1

        for m in range(M):
            for n in range(N):
                if rooms[m][n]==0:
                    bfs(m, n)
                


    
        
        
