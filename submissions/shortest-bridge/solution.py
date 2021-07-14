// https://leetcode.com/problems/shortest-bridge

from collections import defaultdict
class Solution:
    def shortestBridge(self, A):
        island_map = defaultdict(list)
        R, C = len(A), len(A[0])
        def dfs(i, j, val):
            A[i][j] = val
            island_map[val].append((i, j))
            vecs = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
            for vy, vx in vecs:
                if (0 <= vy) and (vy < R) and (0 <= vx) and (vx < C) and (A[vy][vx] == 1):
                    dfs(vy, vx, val)
        
        val = 2
        for r in xrange(R):
            for c in xrange(C):
                if A[r][c] == 1:
                    dfs(r, c, val)
                    val += 1

        ans = float("inf")
        for y2, x2 in island_map[2]:
            for y3, x3 in island_map[3]:
                ans = min(ans, abs(y2 - y3) + abs(x2 - x3) - 1)
        return ans        