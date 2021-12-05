from collections import defaultdict


class Solution:
    def __init__(self):
        self.cnt = 0

    def dfs(self, grid, mat, y, x, idx):
        self.cnt += 1
        R, C = len(grid), len(grid[0])
        mat[y][x] = idx
        for (ny, nx) in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == 1 and mat[ny][nx] == 0:
                self.dfs(grid, mat, ny, nx, idx)

    def largestIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        mat = [[0 for _ in range(C)] for __ in range(R)]
        idx = 1
        idx2area = defaultdict(int)
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1 and mat[r][c] == 0:
                    self.cnt = 0
                    self.dfs(grid, mat, r, c, idx)
                    idx2area[idx] = self.cnt
                    idx += 1

        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    st = set()
                    tmp = 1
                    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                        if 0 <= nr < R and 0 <= nc < C:
                            i = mat[nr][nc]
                            st.add(i)
                    for i in st:
                        tmp += idx2area[i]
                    ans = max(tmp, ans)

        if ans == 0:
            return max(idx2area.values())
        return ans
